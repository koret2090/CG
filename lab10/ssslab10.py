#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt, cos, sin, radians, fabs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import design
import math 
from math import sin, cos, exp, sqrt, pi

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

def angle_transform(x, y, z, angles):
    x, y = rotateX(x, y, z, angles[0])
    x, y = rotateY(x, y, z, angles[1])
    x, y = rotateZ(x, y, z, angles[2])
    return scale(x, y)

# Подпрограмма вычисляет пересечение с горизонтом.
def intersection(x1, y1, x2, y2, arr):
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
def visability(x, y):  # visability point
    global up_change_horizon, bot_change_horizon
    # Если точка, ниже нижнего горизонта (или на нем)
    # То она видима. 
    if y <= bot_change_horizon[x]:
        return -1
    # Если точка выше верхнего горизонта (или на нем)
    # То она видима.
    if y >= up_change_horizon[x]:  
        return 1
    # Иначе она невидима.
    return 0

# Подпрограмма заполнения массивов горизонтов между x1 и x2 
# На основе линейной интерполяции.
def change_horizon(x1, y1, x2, y2):
    global up_change_horizon, bot_change_horizon
    # Проверка вертикальности наклона.
    if (x2 - x1 == 0):
        up_change_horizon[x2] = max(up_change_horizon[x2], y2)
        bot_change_horizon[x2] = min(bot_change_horizon[x2], y2)
        return
    # Иначе вычисляем наклон.
    m = (y2 - y1) / (x2 - x1)
    # Движемся по x с шагом 1, чтобы заполнить 
    # Массивы от x1 до x2.
    for x in range(x1, x2 + 1):
        y = round(m * (x - x1) + y1)
        up_change_horizon[x] = max(up_change_horizon[x], y)
        bot_change_horizon[x] = min(bot_change_horizon[x], y)


# Функция обработки и обновления точек бокового рёбра
def edge_processing(x, y, xe, ye, win):
    if (xe != -1):
        # Если кривая не первая
        win.scene.addLine(xe, ye, x, y)
        change_horizon(xe, ye, x, y)
    xe = x
    ye = y
    return xe, ye

WIDTH = 790
HEIGHT = 640
up_change_horizon = [0] * WIDTH  # Верхний.
bot_change_horizon = [HEIGHT] * WIDTH  # Нижний.
x_points = []
y_points = []
indent_x = 250

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.point = None
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()

    def initUI(self):

        self.show()
        scene = QGraphicsScene(self)
        self.graphicsView.setScene(scene)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scene.setSceneRect(0, 0, WIDTH, HEIGHT)
        pen = QPen(Qt.black, 1)
        
        self.scene = scene
        self.pen = pen

        self.show_btn.clicked.connect(self.prepareForDrawing)

    def Floating_horizon(self, borders_x, x_step, borders_z, z_step, f, angles):
        global up_change_horizon, bot_change_horizon
        # Инициализируем начальными значениями массивы горизонтов.
        up_change_horizon = [0] * WIDTH  # Верхний.
        bot_change_horizon = [HEIGHT] * WIDTH  # Нижний.

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
            x_prev, y_prev = angle_transform(x_prev,y_prev, z, angles)

            flag_prev = visability(x_prev, y_prev)
            #
            x_left, y_left = edge_processing(x_prev, y_prev, x_left, y_left, self)
            x = x_start
            while x <= x_end + x_step / 2:
                y_curr = f(x, z)
                x_curr, y_curr = angle_transform(x, y_curr, z, angles)
                # Проверка видимости текущей точки. 
                flag_curr = visability(x_curr, y_curr)
                # Равенство флагов означает, что обе точки находятся
                # Либо выше верхнего горизонта, либо ниже нижнего,
                # Либо обе невидимы.
                if flag_curr == flag_prev:
                    # Если текущая вершина выше верхнего горизонта
                    # Или ниже нижнего (Предыдущая такая же)
                    if flag_curr != 0:
                        # Значит отображаем отрезок от предыдущей до текущей.
                        self.scene.addLine(x_prev, y_prev, x_curr, y_curr)
                        change_horizon(x_prev, y_prev, x_curr, y_curr)
                    # flag_curr == 0 означает, что и flag_prev == 0,
                    # А значит часть от flag_curr до flag_prev невидима. Ничего не делаем.
                else:
                    # Если видимость изменилась, то
                    # Вычисляем пересечение.
                    if flag_curr == 0:
                        if flag_prev == 1:
                            # Сегмент "входит" в верхний горизонт.
                            # Ищем пересечение с верхним горизонтом.
                            xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, up_change_horizon)
                        else: # flag_prev == -1 (flag_prev нулю (0) не может быть равен, т.к. мы обработали это выше).
                            # Сегмент "входит" в нижний горизонт.
                            # Ищем пересечение с нижним горизонтом.
                            xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, bot_change_horizon)
                        # Отображаем сегмент, от предыдущий точки, до пересечения.
                        self.scene.addLine(x_prev, y_prev, xi, yi)
                        change_horizon(x_prev, y_prev, xi, yi)
                    else:
                        if flag_curr == 1:
                            if flag_prev == 0:
                                # Сегмент "выходит" из верхнего горизонта.
                                # Ищем пересечение с верхним горизонтом. 
                                xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, up_change_horizon)
                                # Отображаем сегмент от пересечения до текущей точки.
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                change_horizon(xi, yi, x_curr, y_curr) 
                            else: # flag_prev == -1
                                # Сегмент начинается с точки, ниже нижнего горизонта
                                # И заканчивается в точке выше верхнего горизонта.
                                # Нужно искать 2 пересечения.
                                # Первое пересечение с нижним горизонтом.
                                xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, bot_change_horizon)
                                # Отображаем сегмент от предыдущей то пересечения.
                                self.scene.addLine(x_prev, y_prev, xi, yi)
                                change_horizon(x_prev, y_prev, xi, yi)
                                # Второе пересечение с верхним горизонтом.
                                xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, up_change_horizon)
                                # Отображаем сегмент от пересечения до текущей.
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                change_horizon(xi, yi, x_curr, y_curr)
                        else: # flag_curr == -1
                            if flag_prev == 0:
                                # Сегмент "выходит" из нижнего горизонта.
                                # Ищем пересечение с нижним горизонтом.
                                xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, bot_change_horizon)
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                change_horizon(xi, yi, x_curr, y_curr)  
                            else:
                                # Сегмент начинается с точки, выше верхнего горизонта
                                # И заканчивается в точке ниже нижнего горизонта.
                                # Нужно искать 2 пересечения.
                                # Первое пересечение с верхним горизонтом.
                                xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, up_change_horizon)
                                # Отображаем сегмент от предыдущей до пересечения.
                                self.scene.addLine(x_prev, y_prev, xi, yi)
                                change_horizon(x_prev, y_prev, xi, yi)
                                # Ищем второе пересечение с нижним горизонтом.
                                xi, yi = intersection(x_prev, y_prev, x_curr, y_curr, bot_change_horizon)
                                # Отображаем сегмент от пересечения до текущей.
                                self.scene.addLine(xi, yi, x_curr, y_curr)
                                change_horizon(xi, yi, x_curr, y_curr)
                x_prev, y_prev = x_curr, y_curr
                flag_prev = flag_curr
                x += x_step
            x_right, y_right = edge_processing(x_prev, y_prev, x_right, y_right, self)
            z -= z_step

    def prepareForDrawing(self):
        self.scene.clear()
        bordersForX = [self.x_start.value(), self.x_end.value()]
        stepForX = self.x_step.value()
        
        bordersForX = [self.z_start.value(), self.z_end.value()]
        stepForZ = self.z_step.value()
        
        angles = [self.x_rotate.value(), self.y_rotate.value(), self.z_rotate.value()]
        
        function = checkFunc(self)
        
        self.Floating_horizon(bordersForX, stepForX, bordersForX, stepForZ, function, angles)

def checkFunc(win):
    if win.funcs_box.currentText() == 'cos(x) * sin(z)':
        return firstFunc
    elif win.funcs_box.currentText() == 'cos(x) + sin(z)':
        return secondFunc
    elif win.funcs_box.currentText() == 'sin(x * z)':
        return thirdFunc
    elif win.funcs_box.currentText() == 'x + z':
        return fourthFunc

def firstFunc(x, z):
    return cos(x) * sin(z)

def secondFunc(x, z):
    return cos(x) + sin(z)

def thirdFunc(x, z):
    return sin(x * z)

def fourthFunc(x, z):
    return x + z        
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()


    #sys.exit(app.exec_())