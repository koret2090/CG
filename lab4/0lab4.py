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
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scene.setSceneRect(0, 0, 720, 500)
        pen = QPen(Qt.black, 1)
        
        self.scene = scene
        self.pen = pen

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

        self.change_thickness.clicked.connect(self.thickness_change)

        self.x_centre = 0
        self.y_centre = 0

        self.clear_btn.clicked.connect(self.scene.clear)
        self.build_circle.clicked.connect(self.building_circle)

        #self.canon_circle(300, 300, 100)
        #self.parametric_circle(300, 200, 100)
        #self.lib_circle(300, 200, 100)
        #self.brezenhem_circle(300, 200, 100)
        #self.mid_point_circle(300, 200, 100)
        
        #self.canon_ellipse(300, 200, 100, 200)
        #self.parametric_ellipse(300, 250, 100, 200)
        self.brezenhem_ellipse(300, 250, 100, 200)

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

    def draw_point_circle(self, cx, cy, x, y):
        self.scene.addLine(cx + x, cy + y, cx + x, cy + y, self.pen)
    
    def draw_point_ellipse(self, cx, cy, x, y):
        self.scene.addLine(cx + x, cy + y, cx + x, cy + y, self.pen)

    def draw_point_canon(self, cx, cy, x, y):
        self.scene.addLine(cx + x, cy + y, cx + x, cy + y, self.pen)
    
    def draw_point_paramateric(self, cx, cy, x, y):
        self.scene.addLine(cx + x, cy + y, cx + x, cy + y, self.pen)

    
    def building_circle(self):
        x_centre = self.x_centre_circle.value()
        y_centre = self.y_centre_circle.value()
        radius = self.radius_circle.value()

        if self.brezenhem_radio.isChecked():
            self.brezenhem_circle(x_centre, y_centre, radius)
        
        elif self.mid_point_radio.isChecked():
            self.mid_point_circle(x_centre, y_centre, radius)
        
        elif self.canon_radio.isChecked():
            self.canon_circle(x_centre, y_centre, radius)
        
        elif self.parametric_radio.isChecked():
            self.parametric_circle(x_centre, y_centre, radius)
        
        elif self.library_radio.isChecked():
            self.lib_circle(x_centre, y_centre, radius)
    
    def canon_circle(self, x_centre, y_centre, radius):
        i = 0
        sqr_radius = radius**2
        
        while i <= radius:
            sqr_i = i * i
            y = round(sqrt(sqr_radius - sqr_i))
            # по октанам
            self.draw_point_circle(x_centre, y_centre, i, y)
            self.draw_point_circle(x_centre, y_centre, i, -y)
            self.draw_point_circle(x_centre, y_centre, -i, y)
            self.draw_point_circle(x_centre, y_centre, -i, -y)
        
            x = round(sqrt(sqr_radius - sqr_i))
            self.draw_point_circle(x_centre, y_centre, x, i)
            self.draw_point_circle(x_centre, y_centre, x, -i)
            self.draw_point_circle(x_centre, y_centre, -x, i)
            self.draw_point_circle(x_centre, y_centre, -x, -i)
            i += 1
        
    
    def parametric_circle(self, x_centre, y_centre, radius):
        length = round(math.pi * radius / 2)
        i = 0
        
        while i <= length:
            angle = i / radius
            x = round(radius * cos(angle))
            y = round(radius * sin(angle))
            self.draw_point_circle(x_centre, y_centre, x, y)
            self.draw_point_circle(x_centre, y_centre, x, -y)
            self.draw_point_circle(x_centre, y_centre, -x, y)
            self.draw_point_circle(x_centre, y_centre, -x, -y)
            i += 1
        

    def lib_circle(self, x_centre, y_centre, radius):
        self.scene.addEllipse(x_centre - radius, y_centre - radius, 2 * radius, 2 * radius, self.pen)



    def brezenhem_circle(self, x_centre, y_centre, radius):           
        x = 0   # задание начальных значений
        y = radius
        delta_i = 2 * (1 - radius)
        while y >= 0:
            # высвечивание текущего пиксела в каждой четверти
            self.draw_point_circle(x_centre, y_centre, x, y)
            self.draw_point_circle(x_centre, y_centre, x, -y)
            self.draw_point_circle(x_centre, y_centre, -x, y)
            self.draw_point_circle(x_centre, y_centre, -x, -y)
            
            # пиксел внутри окружности
            if delta_i < 0:
                x += 1
                sigma = 2 * (delta_i + y) - 1
                if sigma < 0:
                    # горизонтальный шаг
                    delta_i = delta_i + 2 * x + 1
                else:
                    # диагональный шаг
                    y -= 1
                    delta_i = delta_i + 2 * (x - y + 1)
            
            # пиксел вне окружности
            elif delta_i > 0:
                sigma = 2 * (delta_i - x) - 1
                y -= 1
                if sigma < 0:
                    # диагональный шаг
                    x += 1
                    delta_i = delta_i + 2 * (x - y + 1)
                else:
                    # вертикальный шаг
                    delta_i = delta_i - 2 * y + 1
            
            # пиксел лежит на окружности
            else:
                # диагональный шаг
                x += 1
                y -= 1
                delta_i = delta_i + 2 * (x - y + 1)
        

    def mid_point_circle(self, x_centre, y_centre, radius):
        x = 0  # начальные значения
        y = radius
        p = 5 / 4 - radius  # (x + 1)^2 + (y - 1/2)^2 - r^2
        while x <= y:
            self.draw_point_circle(x_centre, y_centre, x, y)
            self.draw_point_circle(x_centre, y_centre, x, -y)
            self.draw_point_circle(x_centre, y_centre, -x, y)
            self.draw_point_circle(x_centre, y_centre, -x, -y)

            self.draw_point_circle(x_centre, y_centre, y, x)
            self.draw_point_circle(x_centre, y_centre, y, -x)
            self.draw_point_circle(x_centre, y_centre, -y, x)
            self.draw_point_circle(x_centre, y_centre, -y, -x)

            x += 1

            if p < 0: 
                p += 2 * x + 1
            else:   
                p += 2 * (x - y) + 5
                y -= 1
    

    def canon_ellipse(self,  x_centre, y_centre, coef_a, coef_b):
        i = 0
        coef_a_sqr = coef_a * coef_a
        while i <= coef_a:
            y = round(coef_b * sqrt(1.0 - i**2 / coef_a_sqr))
            self.draw_point_ellipse(x_centre, y_centre, i, y)
            self.draw_point_ellipse(x_centre, y_centre, i, -y)
            self.draw_point_ellipse(x_centre, y_centre, -i, y)
            self.draw_point_ellipse(x_centre, y_centre, -i, -y)
            i += 1
        
        i = 0
        coef_b_sqr = coef_b * coef_b
        while i <= coef_b:
            x = round(coef_a * sqrt(1.0 - i**2 / coef_b_sqr))
            self.draw_point_ellipse(x_centre, y_centre, x, i)
            self.draw_point_ellipse(x_centre, y_centre, x, -i)
            self.draw_point_ellipse(x_centre, y_centre, -x, i)
            self.draw_point_ellipse(x_centre, y_centre, -x, -i)
            i += 1
    
    def parametric_ellipse(self,  x_centre, y_centre, coef_a, coef_b):
        m = max(coef_a, coef_b)
        length = round(math.pi * m / 2)
        i = 0
        
        while i <= length:
            angle = i / m
            x = round(coef_a * cos(angle))
            y = round(coef_b * sin(angle))
            self.draw_point_ellipse(x_centre, y_centre, x, y)
            self.draw_point_ellipse(x_centre, y_centre, x, -y)
            self.draw_point_ellipse(x_centre, y_centre, -x, y)
            self.draw_point_ellipse(x_centre, y_centre, -x, -y)
            i += 1
            

    def brezenhem_ellipse(self,  x_centre, y_centre, coef_a, coef_b):
        x = 0  # задание начальных значений
        y = coef_b
        coef_a = coef_a ** 2
        delta_i = round(coef_b * coef_b / 2 - coef_a * coef_b * 2 + coef_a / 2)
        coef_b = coef_b ** 2
        sumCoefs = coef_a + coef_b
        while y >= 0:
            self.draw_point_ellipse(x_centre, y_centre, x, y)
            self.draw_point_ellipse(x_centre, y_centre, x, -y)
            self.draw_point_ellipse(x_centre, y_centre, -x, y)
            self.draw_point_ellipse(x_centre, y_centre, -x, -y)
            
            # пиксел лежит внутри эллипса
            if delta_i < 0:  
                sigma = 2 * (delta_i + coef_a * y) - coef_a
                x += 1
                if sigma <= 0:
                    # горизотальный шаг 
                    delta_i = delta_i + 2 * coef_b * x + coef_b
                else:
                    # диагональный шаг  
                    y -= 1
                    delta_i = delta_i + 2 * (coef_b * x - coef_a * y) + sumCoefs

            # пиксель лежит вне эллипса    
            elif delta_i > 0:  
                sigma = 2 * (delta_i - coef_b * x) - coef_b
                y -= 1
                if sigma > 0:
                    # вертикальный шаг  
                    delta_i = delta_i - 2 * y * coef_a + coef_a
                else:
                    # диагональный шаг  
                    x += 1
                    delta_i = delta_i + 2 * (x * coef_b - y * coef_a) + sumCoefs
   
            # пиксель лежит на окружности
            else:
                # диагональный шаг  
                x += 1  
                y -= 1
                delta_i = delta_i + 2 * (x * coef_b - y * coef_a) + sumCoefs

    
    def mid_point_ellipse(self,  x_centre, y_centre, coef_a, coef_b):
        x = 0   # начальные положения
        coef_a_sqr = coef_a ** 2
        coef_b_sqr = coef_b ** 2
        y = coef_b
        p = coef_b_sqr - coef_a_sqr * coef_b + 0.25 * coef_a_sqr   # начальное значение параметра принятия решения в области tg<1
    
        while coef_b_sqr * x < coef_a_sqr * y:  # пока тангенс угла наклона меньше 1
            self.drawPointEllipse(x_centre, y_centre, x, y)
            self.drawPointEllipse(x_centre, y_centre, x, -y)
            self.drawPointEllipse(x_centre, y_centre, -x, y)
            self.drawPointEllipse(x_centre, y_centre, -x, -y)

            x += 1

            if p < 0:  # средняя точка внутри эллипса, ближе верхний пиксел, горизонтальный шаг
                p += 2 * coef_b_sqr * x + coef_b_sqr
            else:   # средняя точка вне эллипса, ближе диагональный пиксел, диагональный шаг
                y -= 1
                p += 2 * coef_b_sqr * x - 2 * coef_a_sqr * y + coef_b_sqr

        p = coef_b_sqr * ((x + 0.5) ** 2) + coef_a_sqr * ((y - 1) ** 2) - coef_a_sqr * coef_b_sqr
        # начальное значение параметра принятия решения в области tg>1 в точке (х + 0.5, y - 1) полседнего положения
        
        while y >= 0:
            self.draw_point_ellipse(x_centre, y_centre, x, y)
            self.draw_point_ellipse(x_centre, y_centre, x, -y)
            self.draw_point_ellipse(x_centre, y_centre, -x, y)
            self.draw_point_ellipse(x_centre, y_centre, -x, -y)

            y -= 1

            if p > 0:
                p -= 2 * coef_a_sqr * y + coef_a_sqr
            else:
                x += 1
                p += 2 * (coef_b_sqr * x - coef_a_sqr * y) + coef_a_sqr


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()


    #sys.exit(app.exec_())