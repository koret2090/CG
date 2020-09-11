import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QPointF
from math import sin, cos, exp, sqrt, pi
import design

SCALE = 40

def scale(x, y):
    x *= SCALE
    y *= SCALE
    x += WIDTH // 2
    y += HEIGHT // 2 # - y
    return round(x), round(y)
    
def convers(arg):
    return arg * pi / 180

def rotateX(x, y, z, angle):
    angle = convers(angle)
    y = cos(angle) * y - sin(angle) * z
    return x, y

def rotateY(x, y, z, angle):
    angle = convers(angle)
    x = cos(angle) * x - sin(angle) * z
    return x, y

def rotateZ(x, y, z, angle):
    angle = convers(angle)
    buf = x
    x = cos(angle) * x - sin(angle) * y
    y = cos(angle) * y + sin(angle) * buf
    return x, y

def transform(x, y, z, angles):
    x, y = rotateX(x, y, z, angles[0])
    x, y = rotateY(x, y, z, angles[1])
    x, y = rotateZ(x, y, z, angles[2])
    return scale(x, y)

# Подпрограмма вычисляет пересечение с горизонтом.
def Intersection(x1, y1, x2, y2, arr):
    dx = x2 - x1
    dyc = y2 - y1
    dyp = arr[x2] - arr[x1]
    if dx == 0:
        xi = x2
        yi = arr[x2]
        return xi, yi
    if y1 == arr[x1] and y2 == arr[x2]:
        return x1, y1
    m = dyc / dx
    xi = x1 - round(dx * (y1 - arr[x1]) / (dyc - dyp))
    yi = round((xi - x1) * m + y1)
    return xi, yi

# Подпрограмма, определяющая видимость точки.
# flag:
# 0 - невидима.
# 1 - выше верхнего.
# -1 - ниже нижнего.
def Visible(x, y):  # Visible point
    global top, bottom
    # Если точка, ниже нижнего горизонта (или на нем)
    # То она видима. 
    if y <= bottom[x]:
        return -1
    # Если точка выше верхнего горизонта (или на нем)
    # То она видима.
    if y >= top[x]:  
        return 1
    # Иначе она невидима.
    return 0

# Подпрограмма заполнения массивов горизонтов между x1 и x2 
# На основе линейной интерполяции.
def Horizon(x1, y1, x2, y2):
    global top, bottom
    # Проверка вертикальности наклона.
    if (x2 - x1 == 0):
        top[x2] = max(top[x2], y2)
        bottom[x2] = min(bottom[x2], y2)
        return
    # Иначе вычисляем наклон.
    m = (y2 - y1) / (x2 - x1)
    # Движемся по x с шагом 1, чтобы заполнить 
    # Массивы от x1 до x2.
    for x in range(x1, x2 + 1):
        y = round(m * (x - x1) + y1)
        top[x] = max(top[x], y)
        bottom[x] = min(bottom[x], y)


# Функция обработки и обновления точек бокового рёбра
def Side(x, y, xe, ye, win):
    if (xe != -1):
        # Если кривая не первая
        win.scene.addLine(xe, ye, x, y)
        Horizon(xe, ye, x, y)
    xe = x
    ye = y
    return xe, ye

WIDTH = 1033
HEIGHT = 573
top = [0] * WIDTH  # Верхний.
bottom = [HEIGHT] * WIDTH  # Нижний.

class HorizonApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initScene()

    def initScene(self):
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene(0, 0, 1033, 579)
        self.graphicsView.setScene(self.scene)
        self.scene.setBackgroundBrush(Qt.white)
        self.pen = QPen()
        self.pen.setWidth(1)
        self.pen.setColor(Qt.black)
        
        self.displayButton.clicked.connect(self.prepareForDrawing)

    def FloatHorizon(self, borders_x, x_step, borders_z, z_step, f, angles):
        global top, bottom
        # Инициализируем начальными значениями массивы горизонтов.
        top = [0] * WIDTH  # Верхний.
        bottom = [HEIGHT] * WIDTH  # Нижний.

        x_start = borders_x[0]
        x_end = borders_x[1]

        z_start = borders_z[0]
        z_end = borders_z[1]

        x_left, y_left = -1, -1
        x_right, y_right = -1, -1

        z = z_end
        while z >= z_start - z_step / 2:

            x_prev = x_start
            y_prev = f(x_start, z)
            x_prev, y_prev = transform(x_prev,y_prev, z, angles)

            flag_prev = Visible(x_prev, y_prev)
            #
            x_left, y_left = Side(x_prev, y_prev, x_left, y_left, self)
            x = x_start
            while x <= x_end + x_step / 2:
                y_curr = f(x, z)
                x_curr, y_curr = transform(x, y_curr, z, angles)
                # Проверка видимости текущей точки. 
                flag_curr = Visible(x_curr, y_curr)
                # Равенство флагов означает, что обе точки находятся
                # Либо выше верхнего горизонта, либо ниже нижнего,
                # Либо обе невидимы.
                if flag_curr == flag_prev:
                    # Если текущая вершина выше верхнего горизонта
                    # Или ниже нижнего (Предыдущая такая же)
                    if flag_curr != 0:
                        # Значит отображаем отрезок от предыдущей до текущей.
                        self.scene.addLine(x_prev, y_prev, x_curr, y_curr)
                        Horizon(x_prev, y_prev, x_curr, y_curr)
                    # flag_curr == 0 означает, что и flag_prev == 0,
                    # А значит часть от flag_curr до flag_prev невидима. Ничего не делаем.
                else:
                    # Если видимость изменилась, то
                    # Вычисляем пересечение.
                    if flag_curr == 0:
                        if flag_prev == 1:
                            # Сегмент "входит" в верхний горизонт.
                            # Ищем пересечение с верхним горизонтом.
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top)
                        else: # flag_prev == -1 (flag_prev нулю (0) не может быть равен, т.к. мы обработали это выше).
                            # Сегмент "входит" в нижний горизонт.
                            # Ищем пересечение с нижним горизонтом.
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom)
                        # Отображаем сегмент, от предыдущий точки, до пересечения.
                        self.scene.addLine(x_prev, y_prev, xi, yi)
                        Horizon(x_prev, y_prev, xi, yi)
                    else:
                        if flag_curr == 1:
                            if flag_prev == 0:
                                # Сегмент "выходит" из верхнего горизонта.
                                # Ищем пересечение с верхним горизонтом. 
                                xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top)
                                # Отображаем сегмент от пересечения до текущей точки.
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                Horizon(xi, yi, x_curr, y_curr) 
                            else: # flag_prev == -1
                                # Сегмент начинается с точки, ниже нижнего горизонта
                                # И заканчивается в точке выше верхнего горизонта.
                                # Нужно искать 2 пересечения.
                                # Первое пересечение с нижним горизонтом.
                                xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom)
                                # Отображаем сегмент от предыдущей то пересечения.
                                self.scene.addLine(x_prev, y_prev, xi, yi)
                                Horizon(x_prev, y_prev, xi, yi)
                                # Второе пересечение с верхним горизонтом.
                                xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top)
                                # Отображаем сегмент от пересечения до текущей.
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                Horizon(xi, yi, x_curr, y_curr)
                        else: # flag_curr == -1
                            if flag_prev == 0:
                                # Сегмент "выходит" из нижнего горизонта.
                                # Ищем пересечение с нижним горизонтом.
                                xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom)
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                Horizon(xi, yi, x_curr, y_curr)  
                            else:
                                # Сегмент начинается с точки, выше верхнего горизонта
                                # И заканчивается в точке ниже нижнего горизонта.
                                # Нужно искать 2 пересечения.
                                # Первое пересечение с верхним горизонтом.
                                xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top)
                                # Отображаем сегмент от предыдущей до пересечения.
                                self.scene.addLine(x_prev, y_prev, xi, yi)
                                Horizon(x_prev, y_prev, xi, yi)
                                # Ищем второе пересечение с нижним горизонтом.
                                xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom)
                                # Отображаем сегмент от пересечения до текущей.
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                Horizon(xi, yi, x_curr, y_curr)
                x_prev, y_prev = x_curr, y_curr
                flag_prev = flag_curr
                x += x_step
            x_right, y_right = Side(x_prev, y_prev, x_right, y_right, self)
            z -= z_step

    def prepareForDrawing(self):
        self.scene.clear()
        bordersForX = [self.xFrom.value(), self.xTo.value()]
        stepForX = self.xStep.value()
        
        bordersForX = [self.zFrom.value(), self.zTo.value()]
        stepForZ = self.zStep.value()
        
        angles = [self.rotateX.value(), self.rotateY.value(), self.rotateZ.value()]
        
        function = checkFunc(self)
        
        self.FloatHorizon(bordersForX, stepForX, bordersForX, stepForZ, function, angles)

def checkFunc(win):
    if win.functions.currentText() == 'sin(x) - cos(z) * exp(x)':
        return firstFunc
    else:
        return secondFunc

def firstFunc(x, z):
    return sin(x) - cos(z) * exp(x)

def secondFunc(x, z):
    return cos(x) * sin(z)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HorizonApp() 
    window.show()  
    app.exec_() 

if __name__ == '__main__':  
    main()  