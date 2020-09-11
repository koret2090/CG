import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui, QtCore
from math import sqrt
import design
import copy

def sign(x):
    if not x:
        return 0
    return x / abs(x)

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
        self.inputPolygon = False
        
        self.lines = []
        self.lastPoint = None
        
        self.colorInRect = QtCore.Qt.red
        self.colorOutRect = QtCore.Qt.blue
        
        self.polygon = []
        self.lastEdge = None

    def clearScene(self):
        self.scene.clear()
        self.listWidget.clear()
        
        self.inputBars = False
        self.inputPolygon = False
        
        self.lines = []
        self.lastPoint = None
        
        self.polygon = []
        self.lastEdge = None
        
    def setBars(self):
        if self.inputBars:
            self.pen.setColor(QtCore.Qt.blue)
            self.scene.addLine(self.lines[len(self.lines) - 1].x(), self.lines[len(self.lines) - 1].y(), self.lines[0].x(), self.lines[0].y(), self.pen)
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
        if self.inputPolygon:
            self.pen.setColor(QtCore.Qt.black)
            self.scene.addLine(self.polygon[len(self.polygon) - 1].x(), self.polygon[len(self.polygon) - 1].y(), self.polygon[0].x(), self.polygon[0].y(), self.pen)
            self.inputPolygon = False
            self.pushButton.setDisabled(False)
            self.pushButton_3.setDisabled(False)
            self.pushButton_4.setDisabled(False)
        else:
            self.inputPolygon = True
            self.pushButton.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)

    def addLine(self, point):
        if self.lastPoint == None:
            self.lastPoint = point
            self.lines.append(QtCore.QPointF(point.x(), point.y()))
        else:
            self.pen.setColor(QtCore.Qt.blue)
            self.lines.append(QtCore.QPointF(point.x(), point.y()))
            x = self.lastPoint.x()
            y = self.lastPoint.y()
            self.listWidget.addItem('( ' + str(point.x()) + ' ; ' + str(point.y()) + ' )')
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.lastPoint = point    

    def addEdge(self, point):
        if self.lastEdge == None:
            self.lastEdge = point
            self.polygon.append(QtCore.QPointF(point.x(), point.y()))
        else:
            self.pen.setColor(QtCore.Qt.black)
            self.polygon.append(QtCore.QPointF(point.x(), point.y()))
            x = self.lastEdge.x()
            y = self.lastEdge.y()
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.lastEdge = point

    def addPoint(self, point):
        if self.inputBars:
            self.addLine(point)
        else:
            self.addEdge(point)
    
    def isConvex(self):
        points = self.polygon
        
        flag = True
        
        vo = points[0]
        vi = points[1]
        vn = points[2]

        xFirst = vi.x() - vo.x()
        yFirst = vi.y() - vo.y()

        xSecond = vn.x() - vi.x()
        ySecond = vn.y() - vi.y()
        
        signOrdinate = xFirst * ySecond - xSecond * yFirst
        previous = sign(signOrdinate)
        
        for i in range(2, len(points) - 1):
            if not flag:
                break
            vo = points[i - 1]
            vi = points[i]
            vn = points[i + 1]
            
            # векторное произведение двух векторов
            xFirst = vi.x() - vo.x()
            yFirst = vi.y() - vo.y()

            xSecond = vn.x() - vi.x()
            ySecond = vn.y() - vi.y()
            
            signOrdinate = xFirst * ySecond - xSecond * yFirst
            current = sign(signOrdinate)
            if current != previous:
                flag = 0
            previous = current
        
        vo = points[len(points) - 1]
        vi = points[0]
        vn = points[1]
        xFirst = vi.x() - vo.x()
        yFirst = vi.y() - vo.y()

        xSecond = vn.x() - vi.x()
        ySecond = vn.y() - vi.y()
        
        signOrdinate = xFirst * ySecond - xSecond * yFirst
        current = sign(signOrdinate)
        
        if current != previous:
            flag = 0
        
        return flag * current

    def sutherlandHodgman(self, peaksOfPolygon, peaksOfCutter):
        # peaksOfPolygon массив вершин исходного многоугольника
        # peaksOfCutter массив вершин отсекающего окна
        peaksOfCutter.append(peaksOfCutter[0])
        # resultPolygon массив результирующего многоугольника
        
        # число вершин исходного многоугольника
        countP = len(peaksOfPolygon)
        # число вершин результирующего многоугольника
        # число вершин отсекающего окна
        countW = len(peaksOfCutter)
        intersectionPoint = QtCore.QPointF()
        firstPoint = QtCore.QPointF()
        secondPoint = QtCore.QPointF()
        
        for i in range(countW - 1):
            resultPolygon = list()
            countQ = 0
            for j in range(countP):
                if j == 0:
                    firstPoint = peaksOfPolygon[j]
                else:
                    if self.crossingFact(secondPoint, peaksOfPolygon[j], \
                                                       peaksOfCutter[i], peaksOfCutter[i + 1]):
                        intersectionPoint = self.intersection(secondPoint, peaksOfPolygon[j], \
                                                                                        peaksOfCutter[i], peaksOfCutter[i + 1])  
                        countQ = self.exit(intersectionPoint, countQ, resultPolygon)
                secondPoint = peaksOfPolygon[j]
                if self.visibility(secondPoint, peaksOfCutter[i], peaksOfCutter[i + 1]) > 0:
                    countQ = self.exit(secondPoint, countQ, resultPolygon)
                
                #next j
            
            if countQ != 0:
                if self.crossingFact(secondPoint, firstPoint, \
                                           peaksOfCutter[i], peaksOfCutter[i + 1]):
                    intersectionPoint = self.intersection(secondPoint, firstPoint, \
                                                        peaksOfCutter[i], peaksOfCutter[i + 1])
                    countQ = self.exit(intersectionPoint, countQ, resultPolygon)
            peaksOfPolygon = copy.deepcopy(resultPolygon)
            countP = countQ
        return peaksOfPolygon
                    
    def crossingFact(self, peak1, peak2, edge1, edge2):
        param1 = self.visibility(peak1, edge1, edge2)
        param2 = self.visibility(peak2, edge1, edge2)
        return (param1 < 0 and param2 > 0) or (param1 > 0 and param2 < 0)
    
    def visibility(self, point, peak1, peak2):
        rab1 = (point.x() - peak1.x()) * (peak2.y() - peak1.y())
        rab2 = (point.y() - peak1.y()) * (peak2.x() - peak1.x())
        rab3 = rab1 - rab2
        return sign(rab3)
    
    def intersection(self, peak1, peak2, edge1, edge2):    
        p1 = peak1
        p2 = peak2

        q1 = edge1
        q2 = edge2

        delta = (p2.x() - p1.x()) * (q1.y() - q2.y()) - (q1.x() - q2.x()) * (p2.y() - p1.y())
        delta_t = (q1.x() - p1.x()) * (q1.y() - q2.y()) - (q1.x() - q2.x()) * (q1.y() - p1.y())

        if abs(delta) <= 1e-6:
            return p2

        t = delta_t / delta

        I = QtCore.QPointF()
        I.setX(peak1.x() + (peak2.x() - peak1.x()) * t)
        I.setY(peak1.y() + (peak2.y() - peak1.y()) * t)
        return I
       
    
    def exit(self, peak, countQ, resultPolygon):
        countQ += 1
        resultPolygon.append(peak)
        return countQ
        


    def cutScene(self):
        norm = self.isConvex()
        if not norm:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Отсекатель не выпуклый!")
            return
        polygon = QtGui.QPolygonF(self.sutherlandHodgman(self.lines, self.polygon))
        self.pen.setWidth(2)
        self.pen.setColor(QtCore.Qt.red)
        self.scene.addPolygon(polygon, self.pen)
        self.pen.setWidth(1)
        
      
class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        global window
        if window.inputBars or window.inputPolygon:
            window.addPoint(event.scenePos())

if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    window = CutterApp()  
    window.show()
    app.exec_()