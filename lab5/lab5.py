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
        

    def clear(self):
        self.scene.clear()
        self.points_table.setText('')
        x_points.clear()
        y_points.clear()
    
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
            self.scene.addLine(x_points[0], y_points[0],\
                x_points[amount - 1], y_points[amount - 1], self.pen)

    def mousePressEvent(self, event):
        point = event.pos()
        x = point.x() - indent_x
        y = point.y()

        if (x >= 0):
            self.add_point(x, y)
            self.draw_point(x, y)
            amount = len(x_points)
            if (amount > 1):
                self.last_link_points(amount, x_points, y_points)
        

        
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()


    #sys.exit(app.exec_())