import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QPixmap, QTransform
from PyQt5.QtCore import Qt, QEventLoop, QPointF
import designn

now = None

class App(QtWidgets.QMainWindow, designn.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.scene = MyScene()
        self.scene.setSceneRect(0, 0, 710, 520)
        self.graphicsView.setScene(self.scene)
        self.pen = QPen(Qt.black, 1)

        self.input_bars = False
        self.input_rect = False
        
        self.lines = []
        self.last_point = None
        
        self.color_in_rect = Qt.green
        self.color_out_rect = Qt.blue
        
        self.rect = None

        self.clear_btn.clicked.connect(self.clear)
        self.adding_lines_btn.clicked.connect(self.set_bars)
        self.adding_cutter_btn.clicked.connect(self.set_rect_bars)

    def clear(self):
        self.scene.clear()
        self.points_table.clear()
        self.inputBars = False
        self.inputRect = False
        self.lines = []
        self.lastPoint = None
    
    def set_bars(self):
        if self.input_bars:
            self.input_bars = False
            self.adding_cutter_btn.setDisabled(False)
            self.clear_btn.setDisabled(False)
            self.cut_btn.setDisabled(False)
        else:
            self.input_bars = True
            self.adding_cutter_btn.setDisabled(True)
            self.clear_btn.setDisabled(True)
            self.cut_btn.setDisabled(True)

       

    def set_rect_bars(self):
        global now
        if self.input_rect:
            if now != None:
                buf = self.scene.itemAt(now, QTransform()).rect()
                self.rect = [buf.left(), buf.top(), buf.right(), buf.bottom()]
                print(self.rect)
            
            self.input_rect = False
            self.adding_lines_btn.setDisabled(False)
            self.clear_btn.setDisabled(False)
            self.cut_btn.setDisabled(False)
        else:
            now = None
            self.rect = None
            self.input_rect = True
            self.adding_lines_btn.setDisabled(True)
            self.clear_btn.setDisabled(True)
            self.cut_btn.setDisabled(True)


    def add_point(self, point):  #point - QpointF(x,y)
        if self.last_point == None:
            self.last_point = point
        else:
            self.lines.append([[self.last_point.x(), self.last_point.y()], \
                                                point.x(), point.y()])
            x = self.last_point.x()
            y = self.last_point.y()
            text = '(' + str(x) + ', ' + str(y) + ')\n' + '('\
                 + str(point.x()) + ', ' + str(point.y())  + ')\n----------------------'
            self.points_table.append(text)
            self.pen.setColor(self.color_out_rect)
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.last_point = None
    


    def cut(self):
        print()
    

    def draw_line(self, point1, point2):
        self.scene.addLine(point1.x(), point1.y(), point2.x(), point2.y())

    def get_points(self, line):
        return QPointF(line[0][0], line[0][1]), QPointF(line[1][0], line[1][1])
    
    def simple_cutter_algorithm(self):
        print()
        if (self.lines != [] and self.rect != None):
            self.pen.setColor(self.color_in_rect)

           

            for j in range(len(self.lines)):
                i = 0 # ИлИ жЕ 1
                while True:
                    p1, p2 = self.get_points(self.lines[j])
                    t1 = [0] * 4
                    t2 = [0] * 4
                    
                    t1 = get_code(self.rect, p1)
                    t2 = get_code(self.rect, p2)
                    m = 1e30
                    
                    s1 = sum(t1)
                    s2 = sum(t2)
                    flag = 0
                    dest = 0
                    if s1 == 0 and s2 == 0:
                        self.draw_line(p1, p2)
                        break 
                    
                    if (bitwise_mult(t1, t2) != 0): #отрезок полностью невидим, игнорим
                        break
                    
                    if s1 == 0:
                        i = 1
                        r1 = p1
                        pt = p2
                        dest = 2

                    if s2 == 0:
                        i = 2
                        r1 = p2
                        pt = p1
                        dest = 2

                    
                    if i != 0:
                        if i == 1:
                            r1 = pt
                        else:
                            r2 = pt
                    i += 1
                    if i > 2:
                        self.draw_line(p1, p2)
                        break
                    

                    if dest == 1:



def get_coordinates_pos(rectangle):
    if rectangle[0] > rectangle[2]:
        right_x = rectangle[0]
        left_x = rectangle[2]
    else:
        right_x = rectangle[2]
        left_x = rectangle[0]
    
    if rectangle[1] > rectangle[3]:
        up_y = rectangle[1]
        down_y = rectangle[3]
    else:
        up_y = rectangle[3]
        down_y = rectangle[1]

    return left_x, right_x, up_y, down_y


def get_code(rectangle, point):
    x = point.x()
    y = point.y()
    left_x, right_x, up_y, down_y = get_coordinates_pos(rectangle)

    code_arr = [0] * 4

    if x < left_x:
        code_arr[0] = 1
    if x > right_x:
        code_arr[1] = 1
    if y < down_y:
        code_arr[2] = 1
    if y > up_y:
        code_arr[3] = 1
    
    return code_arr


def bitwise_mult(code_arr1, code_arr2):
    p = 0
    for i in range(4):
        p += code_arr1[i] * code_arr2[i]  # или же & вместо *

    return p 



def is_visible(rectangle, line):
    code_arr1 = get_code(rectangle, line[0])
    code_arr2 = get_code(rectangle, line[1])
    s1 = sum(code_arr1)
    s2 = sum(code_arr2)

    vis = 2 # преположим, что отрезок полувидим

    if not (s1 * s2):
        vis = 0
    else:
        # проверка тривиальной невидимости отрезка
        if bitwise_mult(code_arr1, code_arr2) != 0:
            vis = 1
    
    return vis # 0 = видимый; 1 = невидимый; 2 = частично видимый


class MyScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        global window
        if window.input_bars:
            window.add_point(event.scenePos())

    def mouseMoveEvent(self, event):
        global window, now
        if window.input_rect:
            if now is None:
                now = event.scenePos()
            else:
                self.removeItem(self.itemAt(now, QTransform()))
                points = event.scenePos()
                self.addRect(now.x(), now.y(), abs(now.x() - points.x()), abs(now.y() - points.y()), window.pen)
            


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()  
    window.show()
    app.exec_()