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
        
        self.color_in_rect = Qt.red
        self.color_out_rect = Qt.blue
        self.color_rect = Qt.green
        
        self.rect = None

        self.clear_btn.clicked.connect(self.clear)
        self.adding_lines_btn.clicked.connect(self.set_bars)
        self.adding_cutter_btn.clicked.connect(self.set_rect_bars)
        self.cut_btn.clicked.connect(self.cut)

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
            
            self.input_rect = False
            self.adding_lines_btn.setDisabled(False)
            self.clear_btn.setDisabled(False)
            self.cut_btn.setDisabled(False)
        else:
            self.pen.setColor(self.color_out_rect)
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
                                                [point.x(), point.y()]])
            x = self.last_point.x()
            y = self.last_point.y()
            text = '(' + str(x) + ', ' + str(y) + ')\n' + '('\
                 + str(point.x()) + ', ' + str(point.y())  + ')\n----------------------'
            self.points_table.append(text)
            self.pen.setColor(self.color_out_rect)
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.last_point = None
    


    def cut(self):
        self.simple_cutter_algorithm()
    

    def draw_line(self, point1, point2):
        self.scene.addLine(point1.x(), point1.y(), point2.x(), point2.y(), self.pen)

    def get_points(self, line):
        return QPointF(line[0][0], line[0][1]), QPointF(line[1][0], line[1][1])
    
    def simple_cutter_algorithm(self):
        # Проверка на существование отрезков и отсекателя
        if (self.lines != [] and self.rect != None):
            # получение исходных данных
            self.pen.setColor(self.color_in_rect)
            left_x, right_x, up_y, down_y = get_coordinates_pos(self.rect)
            
            # проверяем все отрезки
            for j in range(len(self.lines)):
                # установка номера шага(точки) отсечения
                i = 0

                # установка флага
                flag = -1 # невидимый

                # получение координат точек концов отрезка 
                p1, p2 = self.get_points(self.lines[j])       
                r1 = p1
                r2 = p2

                # вычисление кодов концов отрезка Т1, T2 
                t1 = [0] * 4
                t2 = [0] * 4  
                t1 = get_code(self.rect, p1)
                t2 = get_code(self.rect, p2)
                
                # предположение вертикальности отрезка
                m = 1e30
                
                # вычисление S1 и S2
                s1 = sum(t1)
                s2 = sum(t2)

                # вычисление P
                p = bitwise_mult(t1, t2)
                while True:

                    # проверка отрезка на полную видимость
                    if s1 == 0 and s2 == 0:
                        self.draw_line(p1, p2) # высвечиваем
                        break # переходим к следующему отрезку
                    
                    # проверка отрезка на полную невидимость P <> 0
                    if (p != 0): #логическое произведение концов отрезка
                        break # пропускаем отрезок и переходим к следующему
                    
                    # проверка на видимость точки P1 
                    if s1 == 0 and i < 2:
                        r1 = p1
                        p_current = p2
                        i = 2
                    else:
                        # проверка на видимость точки P2
                        if s2 == 0 and i < 2:
                            r1 = p2
                            p_current = p1
                            i = 2

                    # если i > 2 и флаг видимости, то высвечиваем
                    if i > 2 and flag:
                        self.draw_line(r1, r2) # высвечиваем
                        break # переходим к следующему отрезку

                    # переход к нужной точке
                    i += 1
                    p_current = p1 if i == 1 else p2
                    
                    # проверка на вертикальность (чтоб не было деления на 0) 
                    # (если не вертикален, то сразу к пересеч. с верх и нижн. границами)
                    if p1.x() != p2.x():
                        m = (p2.y() - p1.y()) / (p2.x() - p1.x())

                        # проверка на пересечение с левой границей
                        if p_current.x() < left_x:
                            y_cross = m * (left_x - p_current.x()) + p_current.y()
                            
                            # проверка на корректность 
                            if (down_y <= y_cross) and (y_cross <= up_y):
                                if i == 1:
                                    r1.setX(left_x)
                                    r1.setY(y_cross)
                                else:
                                    r2.setX(left_x)
                                    r2.setY(y_cross)
                                flag = 1 # видимый
                        
                        # проверка на пересечение с правой границей
                        elif p_current.x() > right_x:
                            y_cross = m * (right_x - p_current.x()) + p_current.y()
                            
                            # проверка на корректность
                            if (down_y <= y_cross) and (y_cross <= up_y):
                                if i == 1:
                                    r1.setX(right_x)
                                    r1.setY(y_cross)
                                else:
                                    r2.setX(right_x)
                                    r2.setY(y_cross)
                                flag = 1 # видимый
                    
                    # проверка на горизонтальность (чтоб не было деления на m = 0)
                    if (p2.y() != p1.y()):
                        # проверка на пересечение с нижней границей
                        if p_current.y() < down_y:
                            x_cross = 1 / m * (down_y - p_current.y()) + p_current.x()
                            
                            # проверка на корректность
                            if (left_x <= x_cross) and (x_cross <= right_x):
                                if i == 1:
                                    r1.setX(x_cross)
                                    r1.setY(down_y)
                                else:
                                    r2.setX(x_cross)
                                    r2.setY(down_y)
                                flag = 1 # видимый
                        
                        # проверка на пересечение с верхней границей
                        elif p_current.y() > up_y:
                            x_cross = 1 / m * (up_y - p_current.y()) + p_current.x()

                            # проверка на корректность
                            if (left_x <= x_cross) and (x_cross <= right_x):
                                if i == 1:
                                    r1.setX(x_cross)
                                    r1.setY(up_y)
                                else:
                                    r2.setX(x_cross)
                                    r2.setY(up_y)
                                flag = 1 # видимый                                 



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
                self.addRect(now.x(), now.y(), abs(now.x() - points.x()), abs(now.y() - points.y()), QPen(Qt.green, 1))
            


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()  
    window.show()
    app.exec_()