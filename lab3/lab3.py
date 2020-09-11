#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt, cos, sin, radians, fabs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import design
import random
import numpy as np


def sign(var):
    if var == 0:
        return var
    else:
        return var / abs(var)



class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.point = None
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()

    def initUI(self):

        self.statusBar()
        self.show()
        scene = QGraphicsScene(self)
        self.graphicsView.setScene(scene)
        #self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scene.setSceneRect(0, 0, 1010, 510)
        pen = QPen(Qt.black, 1)
        
        self.scene = scene
        self.pen = pen

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

        self.change_thickness.clicked.connect(self.thickness_change)

        self.build_line.clicked.connect(self.line_build)
        self.build_sun.clicked.connect(self.build_lines_in_circle)
        self.clear_btn.clicked.connect(self.scene.clear)



    # Смена цвета фона
    def colour_bg_white(self):
        self.scene.setBackgroundBrush(Qt.white)
    
    def colour_bg_blue(self):
        self.scene.setBackgroundBrush(Qt.blue)
    
    def colour_bg_red(self):
        self.scene.setBackgroundBrush(Qt.red)
    
    def colour_bg_green(self):
        self.scene.setBackgroundBrush(Qt.green)
    
    def colour_bg_black(self):
        self.scene.setBackgroundBrush(Qt.black)
    
    # Смена цвета карандаша
    def colour_line_black(self):
        self.pen.setColor(Qt.black)
    
    def colour_line_blue(self):
        self.pen.setColor(Qt.blue)
    
    def colour_line_red(self):
        self.pen.setColor(Qt.red)
    
    def colour_line_green(self):
        self.pen.setColor(Qt.green)
    
    def colour_line_white(self):
        self.pen.setColor(Qt.white)
    

    def thickness_change(self):
        thickness = self.brush_thickness.value()
        self.pen.setWidth(thickness)

    def draw_point(self, x, y):
        self.scene.addLine(x, y, x, y, self.pen)
    

    def set_brightness(self, brightness):
        colour = self.pen.color()
        colour.setAlpha(brightness)
        self.pen.setColor(colour)

    def line_build(self):
        x1 = self.x_start.value()
        x2 = self.x_end.value()

        y1 = self.y_start.value()
        y2 = self.y_end.value()

        if self.cda_radio.isChecked():
            self.dda_draw(x1, y1, x2, y2)
        
        elif self.brezenhem_float_radio.isChecked():
            self.brezenhem_float(x1, y1, x2, y2)
        
        elif self.brezenhem_int_radio.isChecked():
            self.brezenhem_int(x1, y1, x2, y2)
        
        elif self.brezenhem_smoothing_radio.isChecked():
            self.brezenhem_smoothing(x1, y1, x2, y2)
        
        elif self.wu_radio.isChecked():
            self.wu(x1, y1, x2, y2)
        
        elif self.library_radio.isChecked():
            self.lib_draw(x1, y1, x2, y2)


    def build_lines_in_circle(self):
        length = self.length.value()
        step = self.step.value()

        x_start = 500
        y_start = 250
        for i in range(0, 360, step):
            cur_x = cos(radians(i)) * length + x_start
            cur_y = sin(radians(i)) * length + y_start

            if cur_x > 499. and cur_x < 501.: # КОСТЫЛЬ
                cur_x = 500 

            if self.cda_radio.isChecked():
                self.dda_draw(x_start, y_start, cur_x, cur_y)
        
            elif self.brezenhem_float_radio.isChecked():
                self.brezenhem_float(x_start, y_start, cur_x, cur_y)
            
            elif self.brezenhem_int_radio.isChecked():
                self.brezenhem_int(x_start, y_start, cur_x, cur_y)
            
            elif self.brezenhem_smoothing_radio.isChecked():
                self.brezenhem_smoothing(x_start, y_start, cur_x, cur_y)

            elif self.wu_radio.isChecked():
                self.wu(x_start, y_start, cur_x, cur_y)
            
            elif self.library_radio.isChecked():
                self.lib_draw(x_start, y_start, cur_x, cur_y)

    def lib_draw(self, x_start, y_start, x_end, y_end):
        self.scene.addLine(x_start, y_start, x_end, y_end, self.pen)

    def dda_draw(self, x_start, y_start, x_end, y_end):
        if (x_start == x_end) and (y_start == y_end):
            self.draw_point(x_start, y_start)
        else:
            delta_x = x_end - x_start
            delta_y = y_end - y_start

            dx = abs(delta_x)
            dy = abs(delta_y)

            length = dy
            if dx > dy:
                length = dx 
            
            x = x_start
            y = y_start

            delta_x = delta_x / length
            delta_y = delta_y / length     

            i = 1
            while i <= length:
                self.draw_point(round(x), round(y))
                x += delta_x
                y += delta_y
                i += 1
            
            '''
            length = max(abs(x_start - x_end), abs(y_start - y_end))

            if length == 0:
                self.draw_point(x_start, y_start)
            else:
                dX = (x_end - x_start) / length
                dY = (y_end - y_start) / length

                x = x_start
                y = y_start

                while length > 0:
                    self.draw_point(round(x), round(y))
                    x += dX 
                    y += dY
                    length -= 1
            '''
    def brezenhem_float(self, x_start, y_start, x_end, y_end):
        if x_start == x_end and y_start == y_end:
            self.draw_point(x_start, y_start)
        else:
            dx = x_end - x_start
            dy = y_end - y_start
            sign_x = sign(dx)
            sign_y = sign(dy)

            dx = abs(dx)
            dy = abs(dy)

            change = 0
            if dx <= dy:
                change = 1
                dx, dy = dy, dx
            
            m = dy / dx
            e = m - 0.5
            x = x_start
            y = y_start

            i = 1
            while i <= dx:
                self.draw_point(x, y)
                if (e > 0):
                    if (change):
                        x += sign_x
                    else:
                        y += sign_y
                    e -= 1
                if (e <= 0):
                    if (change):
                        y += sign_y
                    else:
                        x += sign_x
                e += m
                
                i += 1
    
    def brezenhem_int(self, x_start, y_start, x_end, y_end):
        if x_start == x_end and y_start == y_end:
            self.draw_point(x_start, y_start)
        else:
            dx = x_end - x_start
            dy = y_end - y_start
            sign_x = sign(dx)
            sign_y = sign(dy)

            dx = abs(dx)
            dy = abs(dy)

            change = 0
            if dx <= dy:
                change = 1
                dx, dy = dy, dx      
            
            e = 2 * dy - dx
            x = x_start
            y = y_start

            i = 1
            while i <= dx:
                self.draw_point(x, y)
                if (e > 0):
                    if (change):
                        x += sign_x
                    else:
                        y += sign_y
                    e -= 2 * dx
                if (e <= 0):
                    if (change):
                        y += sign_y
                    else:
                        x += sign_x
                    e += 2 * dy
                
                i += 1
    
    def brezenhem_smoothing(self, x_start, y_start, x_end, y_end):
        if x_start == x_end and y_start == y_end:
            self.draw_point(x_start, y_start)
        else:
            dx = x_end - x_start
            dy = y_end - y_start
            sign_x = sign(dx)
            sign_y = sign(dy)
            I = 255

            dx = abs(dx)
            dy = abs(dy)

            if dx != 0:
                h = dy / dx
            else:
                h = 0

           
            change = 0
            if dx <= dy:
                change = 1
                dx, dy = dy, dx
                if h:
                    h = 1 / h 
            
            h *= I
            e = I / 2
            w = I - h
            i = 1
            
            x = x_start
            y = y_start

            while i <= dx:
                self.set_brightness(255 - e)
                
                self.draw_point(x, y)

                if e <= w:
                    if change:
                        y += sign_y
                    else:
                        x += sign_x
                    
                    e += h

                else:
                    x += sign_x
                    y += sign_y
                    e -= w
                
                i += 1
        
        self.set_brightness(I)
    
    def wu(self, x_start, y_start, x_end, y_end):
        if x_start == x_end and y_start == y_end:
            self.draw_point(x_start, y_start)
        else:
            x_beginning  = x_start
            y_beginning = y_start
            x_finish = x_end
            y_finish = y_end

            dx = x_end - x_start
            dy = y_end - y_start

            change = 0
            if abs(dx) < abs(dy):
                change = 1
                x_beginning, y_beginning = y_beginning, x_beginning
                x_finish, y_finish = y_finish, x_finish
                dx, dy = dy, dx

            if x_finish < x_beginning:
                x_beginning, x_finish = x_finish, x_beginning
                y_beginning, y_finish = y_finish, y_beginning
            
            degrees = 0
            if dx != 0:
                degrees = dy / dx
            
            y = y_beginning
            x = x_beginning
            I = 255

            while x <= x_finish:
                if change:
                    sign_y = sign(y)
                    brightness = I - I * (fabs(y - int(y)))
                    self.set_brightness(brightness)
                    self.draw_point(y, x)

                    if dy and dx:
                        brightness = I - I * (fabs(y - int(y)))
                        self.set_brightness(brightness)
                        self.draw_point(y, x)
                    
                    self.draw_point(y + sign_y, x)
                else:
                    sign_y = sign(y)
                    brightness = I - I * (fabs(y - int(y)))
                    self.set_brightness(brightness)
                    self.draw_point(x, y)

                    if dy and dx:
                        brightness = I - I * (fabs(y - int(y)))
                        self.set_brightness(brightness)
                        self.draw_point(x, y)
                    self.draw_point(x, y + sign_y)
                y += degrees
                x += 1
            
            self.set_brightness(I)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()


    #sys.exit(app.exec_())