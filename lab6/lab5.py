#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer, QEventLoop, pyqtSignal
import design1
import time

x_points = []
y_points = []
indent_x = 250

class App(QtWidgets.QMainWindow, design1.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.x_seed = -1
        self.y_seed = -1

        self.is_ended = False
        self.ended_index = 0

        self.seed_adding_flag = False
        self.ends_colour = Qt.darkYellow
        self.stack = []

        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()

        

    def initUI(self):

        self.statusBar()
        self.show()
        scene = QGraphicsScene(self)
        self.graphicsView.setScene(scene)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scene.setSceneRect(0, 0, 710, 520)
        pen = QPen(Qt.black, 1)
        
        self.scene = scene
        self.pen = pen

        self.scene.setBackgroundBrush(Qt.white)
        self.image = QImage(710, 520, QImage.Format_ARGB32_Premultiplied)
        self.bg_colour = Qt.white
        self.pen_colour = Qt.black
        self.image.fill(self.bg_colour)

        #self.scene.addLine(0,0, 400, 400, self.pen)

        self.make_bg_white.clicked.connect(self.colour_bg_white)
        self.make_bg_blue.clicked.connect(self.colour_bg_blue)
        self.make_bg_red.clicked.connect(self.colour_bg_red)
        self.make_bg_green.clicked.connect(self.colour_bg_green)
        self.make_bg_black.clicked.connect(self.colour_bg_black)

        self.make_line_black.clicked.connect(self.colour_line_black)
        self.make_line_blue.clicked.connect(self.colour_line_blue)
        self.make_line_red.clicked.connect(self.colour_line_red)
        self.make_line_green.clicked.connect(self.colour_line_green)
        self.make_line_white.clicked.connect(self.colour_line_white)

        self.clear_btn.clicked.connect(self.clear)

        self.add_point_btn.clicked.connect(self.add_point_table)
        self.end_btn.clicked.connect(self.end_rectangle)

        self.add_seed_btn.clicked.connect(self.add_seed)
        
        self.fill_btn.clicked.connect(self.start)

    def clear(self):
        self.scene.clear()
        self.points_table.clear()
        self.timing_text.clear()
        x_points.clear()
        y_points.clear()

        self.is_ended = False
        self.ended_index = 0

        self.x_seed = None
        self.y_seed = None

        self.image = QImage(710, 520, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(self.bg_colour)
    
    # Смена цвета фона
    def colour_bg_white(self):
        self.scene.setBackgroundBrush(Qt.white)
        self.bg_colour = Qt.white
    
    def colour_bg_blue(self):
        self.scene.setBackgroundBrush(Qt.blue)
        self.bg_colour = Qt.blue
    
    def colour_bg_red(self):
        self.scene.setBackgroundBrush(Qt.red)
        self.bg_colour = Qt.red
    
    def colour_bg_green(self):
        self.scene.setBackgroundBrush(Qt.green)
        self.bg_colour = Qt.green
    
    def colour_bg_black(self):
        self.scene.setBackgroundBrush(Qt.black)
        self.bg_colour = Qt.black
    
    # Смена цвета карандаша
    def colour_line_black(self):
        self.pen.setColor(Qt.black)
        self.pen_colour = Qt.black
    
    def colour_line_blue(self):
        self.pen.setColor(Qt.blue)
        self.pen_colour = Qt.blue
    
    def colour_line_red(self):
        self.pen.setColor(Qt.red)
        self.pen_colour = Qt.red
    
    def colour_line_green(self):
        self.pen.setColor(Qt.green)
        self.pen_colour = Qt.green
    
    def colour_line_white(self):
        self.pen.setColor(Qt.white)
        self.pen_colour = Qt.white

    def draw_point(self, x, y):
        self.scene.addLine(x, y, x, y, self.pen)
    
    def add_point_table(self):
        x = self.x_point_box.value()
        y = self.y_point_box.value()
        self.add_point(x, y)
        self.draw_point(x, y)
        
        amount = len(x_points)
        if (amount > 1):
            self.last_link_points(amount, x_points, y_points)
           
    def add_point(self, x, y):
        x_points.append(x)
        y_points.append(y)
        text = '(' + str(x) + ', ' + str(y) + ')'
        self.points_table.append(text)

        #self.lbl.setText(text)


    def last_link_points(self, amount, x_points, y_points):
        self.scene.addLine(x_points[amount - 2], y_points[amount - 2],\
             x_points[amount - 1], y_points[amount - 1], self.pen)

    
    def end_rectangle(self):
        amount = len(x_points)
        if (amount > 1):
            self.scene.addLine(x_points[self.ended_index], y_points[self.ended_index],\
                x_points[amount - 1], y_points[amount - 1], self.pen)
        
        x_points.append(-1)
        y_points.append(-1)
        self.ended_index = len(x_points)
        self.is_ended = True

    def mousePressEvent(self, event):
        point = event.pos()
        x = point.x() - indent_x
        y = point.y()

        if (x >= 0 and y < 520):
            if (not self.seed_adding_flag):
                self.add_point(x, y)
                self.draw_point(x, y)
                amount = len(x_points)
                if (amount > 1 and not self.is_ended):
                    self.last_link_points(amount, x_points, y_points)

                self.is_ended = False
            else:
                self.save_seed(x, y)


    def draw_edges_end(self):
        end_index = 0

        edge = self.pen_colour
        my_painter = QPainter()
        my_painter.begin(self.image)
        my_painter.setPen(QPen(edge))

        i = 0
        while i < (len(x_points) - 1):
            if (x_points[i+1] != -1):               
                my_painter.drawLine(x_points[i], y_points[i], x_points[i+1], y_points[i+1])
                #self.scene.addLine(x_points[i], y_points[i], x_points[i+1], y_points[i+1], self.pen)
                #print("DRAW ", x_points[i], y_points[i], x_points[i+1], y_points[i+1])
            else:
                my_painter.drawLine(x_points[i], y_points[i], x_points[end_index], y_points[end_index])
                #self.scene.addLine(x_points[i], y_points[i], x_points[end_index], y_points[end_index], self.pen)
                #print("DRAW ", x_points[i], y_points[i], x_points[end_index], y_points[end_index])
                i += 1
                end_index = i+1
                          
            i += 1
        
        if (end_index == 0):
            my_painter.drawLine(x_points[i], y_points[i], x_points[0], y_points[0],)
            #self.scene.addLine(x_points[i], y_points[i], x_points[0], y_points[0], self.pen)
            #print("DRAW ", x_points[i], y_points[i], x_points[0], y_points[0])
        
        my_painter.end()

    
    def draw_edges(self):
        end_index = 0

        edge = self.ends_colour
        my_painter = QPainter()
        my_painter.begin(self.image)
        my_painter.setPen(QPen(edge))

        i = 0
        while i < (len(x_points) - 1):
            if (x_points[i+1] != -1):               
                my_painter.drawLine(x_points[i], y_points[i], x_points[i+1], y_points[i+1])
                #self.scene.addLine(x_points[i], y_points[i], x_points[i+1], y_points[i+1], self.pen)
                #print("DRAW ", x_points[i], y_points[i], x_points[i+1], y_points[i+1])
            else:
                my_painter.drawLine(x_points[i], y_points[i], x_points[end_index], y_points[end_index])
                #self.scene.addLine(x_points[i], y_points[i], x_points[end_index], y_points[end_index], self.pen)
                #print("DRAW ", x_points[i], y_points[i], x_points[end_index], y_points[end_index])
                i += 1
                end_index = i+1
                          
            i += 1
        
        if (end_index == 0):
            my_painter.drawLine(x_points[i], y_points[i], x_points[0], y_points[0],)
            #self.scene.addLine(x_points[i], y_points[i], x_points[0], y_points[0], self.pen)
            #print("DRAW ", x_points[i], y_points[i], x_points[0], y_points[0])
        
        my_painter.end()




    def start(self):
        if (self.x_seed == -1):
            QMessageBox.warning(self, "Ошибка!","Затравочный пиксел не введён")
        else:
            if self.delay.isChecked():
                self.algorithm_delayed()
            else:
                self.algorithm()
            self.draw_edges_end()
            pix = QPixmap()
            pix.convertFromImage(self.image)
            self.scene.addPixmap(pix)


    def save_seed(self, x, y):
        self.x_seed = x
        self.y_seed = y
        text = '(' + str(x) + ', ' + str(y) + ')'
        self.seed_coords_lbl.setText(text)
        self.seed_adding_flag = False
        

    def add_seed(self):
        self.is_ended = True
        self.seed_adding_flag = True
        

    def draw_pixel(self, x, y):
        self.scene.addLine(x, y, x, y, self.pen)


    def algorithm(self):
        time_start = time.time()

        # вычерчивание границ области
        self.draw_edges()
        
        pix = QPixmap()
        my_painter = QPainter()
        my_painter.begin(self.image)

        # ввод исходных данных
        ends = self.ends_colour  
        my_painter.setPen(self.pen)       
        stack = []

        # занесение затравочного пиксела в стек
        push(stack, [self.x_seed, self.y_seed])  
        while stack:
            # извлечение пиксела из стека
            current_pixel = pop(stack)
            x = current_pixel[0]
            y = current_pixel[1]
            my_painter.drawPoint(x, y)
            
            # сохраняем х-координату затравочного пиксела
            x_temp = x

            # заполняем интервал справа от затравки
            x += 1
            while self.image.pixelColor(x, y) != ends:
                my_painter.drawPoint(x, y)
                x += 1

            # сохраняем крайний справа пиксел    
            x_right = x - 1

            # восстанавливаем x-координату затравки
            x = x_temp

            # заполняем интервал слева от затравки
            x -= 1
            while self.image.pixelColor(x, y) != ends:
                my_painter.drawPoint(x, y)
                x -= 1
            
            # сохраняем крайний справа пиксел
            x_left = x + 1
            
            
            x = x_left
            y += 1
            while x <= x_right:
                # ищем затравку на строке выше
                flag = 0            
                while self.image.pixelColor(x, y) != ends and \
                    self.image.pixelColor(x, y) != self.pen_colour\
                        and x <= x_right:
                    
                    if flag == 0:
                        flag = 1
                    x += 1

                # помещаем в стек крайний справа пиксел
                if flag == 1:
                    if x == x_right and self.image.pixelColor(x, y) != ends\
                        and self.image.pixelColor(x, y) != self.pen_colour:
                        push(stack, [x, y])
                    else:
                        push(stack, [x - 1, y])
                    
                    flag = 0
                
                 # продолжим проверку, если интервал был прерван
                x_temp = x
                while self.image.pixelColor(x, y) == ends or \
                    self.image.pixelColor(x, y) == self.pen_colour\
                        and x < x_right:
                    x += 1
                
                # удостоверимся, что координата пиксела увеличена
                if x == x_temp:
                    x += 1
            
            # проверяем строку ниже
            # (аналогично строке выше, только нужно опуститься по y)
            x = x_left
            
            # переходим на нижнюю строку
            y -= 2
            while x <= x_right:
                flag = 0            
                while self.image.pixelColor(x, y) != ends and \
                    self.image.pixelColor(x, y) != self.pen_colour\
                        and x <= x_right:
                    if flag == 0:
                        flag = 1
                    x += 1

                if flag == 1:
                    if x == x_right and self.image.pixelColor(x, y) != ends\
                        and self.image.pixelColor(x, y) != self.pen_colour:
                        push(stack, [x, y])
                    else:
                        push(stack, [x - 1, y])
                    
                    flag = 0
                
                x_temp = x
                while self.image.pixelColor(x, y) == ends or \
                    self.image.pixelColor(x, y) == self.pen_colour\
                        and x < x_right:
                    x += 1
                
                if x == x_temp:
                    x += 1
            
        time_process = float(time.time() - time_start)
        self.timing_text.setText(str(round(time_process, 4)))
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)
    

    def algorithm_delayed(self):
        time_start = time.time()

        # вычерчивание границ области
        self.draw_edges()
        
        pix = QPixmap()
        my_painter = QPainter()
        my_painter.begin(self.image)

        ends = self.ends_colour
        my_painter.setPen(self.pen)
        self.draw_edges()
        stack = []
    
        push(stack, [self.x_seed, self.y_seed])  
        while stack:
            current_pixel = pop(stack)
            x = current_pixel[0]
            y = current_pixel[1]
            my_painter.drawPoint(x, y)

            x_temp = x
            x += 1
            #self.image.pixelColor(x, y)
            #sdsself.image.pixelColor(x, y)
            while self.image.pixelColor(x, y) != ends:
                my_painter.drawPoint(x, y)
                #print(1)
                x += 1
            
            x_right = x - 1
            x = x_temp
            x -= 1
            while self.image.pixelColor(x, y) != ends:
                my_painter.drawPoint(x, y)
                #print(2)
                x -= 1
            
            x_left = x + 1
            
            x = x_left
            y += 1
            while x <= x_right:
                #print(3)
                flag = 0            
                while self.image.pixelColor(x, y) != ends and \
                    self.image.pixelColor(x, y) != self.pen_colour\
                        and x < x_right:
                    
                    if flag == 0:
                        flag = 1
                    x += 1

                if flag == 1:
                    if x == x_right and self.image.pixelColor(x, y) != ends\
                        and self.image.pixelColor(x, y) != self.pen_colour:
                        push(stack, [x, y])
                    else:
                        push(stack, [x - 1, y])
                    
                    flag = 0
                
                x_temp = x
                while self.image.pixelColor(x, y) == ends or \
                    self.image.pixelColor(x, y) == self.pen_colour\
                        and x < x_right:
                    x += 1
                
                if x == x_temp:
                    x += 1
            

            x = x_left
            y -= 2
            while x <= x_right:
                #print(4)
                flag = 0            
                while self.image.pixelColor(x, y) != ends and \
                    self.image.pixelColor(x, y) != self.pen_colour\
                        and x < x_right:
                    if flag == 0:
                        flag = 1
                    x += 1

                if flag == 1:
                    if x == x_right and self.image.pixelColor(x, y) != ends\
                        and self.image.pixelColor(x, y) != self.pen_colour:
                        push(stack, [x, y])
                    else:
                        push(stack, [x - 1, y])
                    
                    flag = 0
                
                x_temp = x
                while self.image.pixelColor(x, y) == ends or \
                    self.image.pixelColor(x, y) == self.pen_colour\
                        and x < x_right:
                    x += 1
                
                if x == x_temp:
                    x += 1
            
            loop = QEventLoop()
            QTimer.singleShot(100, loop.quit)
            loop.exec()
            
            pix.convertFromImage(self.image)
            self.scene.addPixmap(pix)
        
        time_process = float(time.time() - time_start)
        self.timing_text.setText(str(round(time_process, 4)))
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)
            

            



def pop(stack):
        value = stack[len(stack) - 1]
        stack.pop(len(stack) - 1)

        return value
    
def push(stack, value):
    stack.append(value)    
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()

    #sys.exit(app.exec_())