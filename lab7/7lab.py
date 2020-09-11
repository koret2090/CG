import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui, QtCore
from math import sqrt
import design

now = None

class CutterApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scene = myScene(10, 10, 871, 541)
        self.graphicsView.setScene(self.scene)
        self.scene.setBackgroundBrush(QtCore.Qt.white)

        self.pushButton.clicked.connect(self.setBars)
        self.pushButton_2.clicked.connect(self.setLines)
        self.pushButton_3.clicked.connect(self.cutScene)
        self.pushButton_4.clicked.connect(self.clearScene)
        
        self.pen = QtGui.QPen()
        self.pen.setWidth(1)
        self.pen.setColor(QtCore.Qt.black)
        self.pen.setWidth(2)
        
        self.inputBars = False
        self.inputRect = False
        
        self.lines = []
        self.lastPoint = None
        
        self.colorInRect = QtCore.Qt.red
        self.colorOutRect = QtCore.Qt.blue
        
        self.rect = None

    def clearScene(self):
        self.scene.clear()
        self.listWidget.clear()
        self.inputBars = False
        self.inputRect = False
        self.lines = []
        self.lastPoint = None
        
    def setBars(self):
        if self.inputBars:
            self.inputBars = False
            self.pushButton_2.setDisabled(False)
            self.pushButton_3.setDisabled(False)
            self.pushButton_4.setDisabled(False)
        else:
            self.inputBars = True
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)

    def setLines(self):
        global now
        if self.inputRect:
            if now != None:
                buf = self.scene.itemAt(now, QtGui.QTransform()).rect()
                self.rect = [buf.left(), buf.top(), buf.right(), buf.bottom()]
                print(self.rect)
            self.inputRect = False
            self.pushButton.setDisabled(False)
            self.pushButton_3.setDisabled(False)
            self.pushButton_4.setDisabled(False)
        else:
            now = None
            self.rect = None 
            self.inputRect = True
            self.pushButton.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)

    def addPoint(self, point):
        if self.lastPoint == None:
            self.lastPoint = point
        else:
            self.lines.append([[self.lastPoint.x(), self.lastPoint.y()], \
                                            [point.x(), point.y()]])
            x = self.lastPoint.x()
            y = self.lastPoint.y()
            self.listWidget.addItem('( (' + str(x) + ' ; ' + str(y) + ') ; (' + \
                                                    str(point.x()) + ' ; ' + str(point.y()) + ') )')
            self.pen.setColor(self.colorOutRect)
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.lastPoint = None    
    
    def drawAllLines(self):
        for i in range(len(self.lines)):
                self.pen.setColor(self.colorOutRect)
                P1 = QtCore.QPointF(self.lines[i][0][0], self.lines[i][0][1])
                P2 = QtCore.QPointF(self.lines[i][1][0], self.lines[i][1][1])
                self.scene.addLine(P1.x(), P1.y(), P2.x(), P2.y(), self.pen)
    
    def cutScene(self):
        # Проверка на существование отрезков и отсекателя
        if (self.lines != [] and self.rect != None):
            # Вывод всех отрезков
            self.pen.setColor(self.colorInRect)
            # Для каждого отрезка
            for j in range(0, len(self.lines)): 
                # Ввод точности ε вычисления точки пересечения отрезка 
                # с границей отсекателя.
                eps = sqrt(2)
                # Установка номера шага отсечения
                i = 1
                # Ввод координат концов отрезка
                P1 = QtCore.QPointF(self.lines[j][0][0], self.lines[j][0][1])
                P2 = QtCore.QPointF(self.lines[j][1][0], self.lines[j][1][1])
                T1 = [0 for i in range(4)]
                T2 = [0 for i in range(4)]
                S1 = 0
                S2 = 0
                while True:
                    # Вычисление кодов концевых точек  
                    # запись их в соответствующие массивы T1 и T2 размерностью 1х4
                    T1 = setBits(self.rect, P1, T1)
                    T2 = setBits(self.rect, P2, T2)
                    # вычисление сумм кодов концов S1 S2
                    S1 = getSum(T1)
                    S2 = getSum(T2)
                    
                    # Проверка полной видимости отрезка. 
                    # Если коды обоих концов отрезка равны нулю (полная видимость отрезка)
                    if S1 == 0 and S2 == 0:
                        # Визуализация отрезка
                        self.scene.addLine(P1.x(), P1.y(), P2.x(), P2.y(), self.pen)
                        break
                    R = QtCore.QPointF()
                    # Проверка полной невидимости отрезка. 
                    # Вычисление побитного логического произведения кодов концевых точек отрезка. 
                    # Если произведение отлично от нуля (отрезок невидим)
                    if (logicMult(T1, T2) != 0):
                        print("yes")
                        break
                    else:
                        # Запоминание исходной точки P1 в промежуточной переменной R.
                        R = P1
                        # Проверка на окончание процесса решения
                        if i > 2:
                            # Вычисление побитного логического произведения кодов концевых точек отрезка. 
                            # Если произведение отлично от нуля (отрезок невидим)
                            if  logicMult(T1, T2) == 0:
                                self.scene.addLine(P1.x(), P1.y(), P2.x(), P2.y(), self.pen)
                                break
                            else:
                                break
                        # Проверка нахождения точки пересечения отрезка с границами отсекателя
                        # Расстояние между концевыми точками исследуемого 
                        # отрезка меньше допустимой погрешности
                        while (abs(P1.x() - P2.x()) > eps or abs(P1.y() - P2.y()) > eps):
                            # Вычисление средней точки Pср. отрезка
                            Pcp = QtCore.QPointF()
                            Pcp.setX((P1.x() + P2.x()) / 2)
                            Pcp.setY((P1.y() + P2.y()) / 2)
                            # Запоминание текущей точки P1
                            Pm = P1
                            # Замена точки P1 на среднюю точку
                            P1 = Pcp
                            # Вычисление нового кода T1 точки P1
                            T1 = setBits(self.rect, P1, T1)
                            # Вычисление произведения pr кодов концов нового отрезка P1P2
                            pr = logicMult(T1, T2)
                            # Проверка полной невидимости отрезка P1P2
                            if pr != 0:
                                # Возврат к предыдущему отрезку P1P2
                                P1 = Pm
                                P2 = Pcp 
                        # Поиск наиболее удаленной от P2 видимой точки отрезка
                        P1 = P2
                        P2 = R
                        # Увеличение шага выполнения отсечения i=i+1
                        i += 1     
        self.pen.setColor(QtCore.Qt.black)
            
def logicMult(arrFirst, arrSecond):
    res = 0
    for i in range(4):
        res += arrFirst[i] * arrSecond[i]
    return res
                    
def getSum(arr):
    res = 0
    for i in range(len(arr)):
        res += arr[i]
    return res

def minAndMax(rect):
    if rect[1] > rect[3]:
        minY = rect[3]
        maxY = rect[1]
    else:
        minY = rect[1]
        maxY= rect[3]
        
    if rect[0] > rect[2]:
        minX = rect[2]
        maxX = rect[0]
    else:
        minX = rect[0]
        maxX = rect[2]
    return minX, maxX, minY, maxY

         
def setBits(rect, point, arr):
    x = point.x()
    y = point.y()
    minX, maxX, minY, maxY = minAndMax(rect)
    arr[3] = 1 if x < minX else 0
    arr[2] = 1 if x > maxX else 0
    arr[1] = 1 if y < minY else 0
    arr[0] = 1 if y > maxY else 0
    return arr             


class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        global window
        if window.inputBars:
            window.addPoint(event.scenePos())
    
    def mouseMoveEvent(self, event):
        global window, now
        if window.inputRect:
            if now is None:
                now = event.scenePos()
            else:
                self.removeItem(self.itemAt(now, QtGui.QTransform()))
                points = event.scenePos()
                self.addRect(now.x(), now.y(), abs(now.x() - points.x()), abs(now.y() - points.y()), window.pen)

if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    window = CutterApp()  
    window.show()
    app.exec_()
