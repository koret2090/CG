#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import design
import random


# НАДО СДЕЛАТЬ КНОПКУ(И) ДЛЯ ОЧИЩЕНИЯ ПОЛЕЙ!!!
X = 20
Y = 10
x_points = [] #array for points' x coordinates
y_points = [] #array for points' y coordinates

x_triangle_points = [] #array for triangle points' x coordinates
y_triangle_points = [] #array for triangle points' y coordinates


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.point = None
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.initUI()

    '''
    def paintEvent(self, event):

        brush = QPainter()
        brush.begin(self)
        brush.setPen(Qt.red)
        brush.drawPoint(X + x_points[len(x_points) - 1], Y + y_points[len(y_points) - 1])
        brush.end()
    '''
    def initUI(self):

        self.pushButton.clicked.connect(self.check_points_entry)
        self.add_triangle.clicked.connect(self.check_triangle_entry)
        self.del_point

        self.statusBar()
        self.show()

    def paintEvent(self, event):
        if self.point == 'Yes':
            print("DIO")
            self.painter = QPainter(self)
            self.painter.setPen(QPen(Qt.red, 5))

            for i in range(len(x_points)):
                self.painter.drawPoint(X + x_points[i],\
                    Y + y_points[i])
            
            self.painter.end()
            self.point = None
            
    '''  
    def drawPoint(self):
        brush = QPainter()
        brush.begin(self)
        brush.setPen(Qt.red)
        brush.drawPoint(X + x_points[len(x_points) - 1], Y + y_points[len(y_points) - 1])
        #brush.end()
        self.update()
    '''
    def delete_points(self):
        self.update()
    
    def check_points_entry(self):

        #sender = self.sender()
        check = True
        x = self.x_points_entry.text()
        y = self.y_points_entry.text()
        if x == '':
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Некорректный ввод!\nВы не ввели координату x.")
        elif y == '':
            check = False
            QMessageBox.warning(self, "Ошибка!",\
                "Некорректный ввод!\nВы не ввели координату y.")
        else: 
            try:
                x = float(x)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля х введено не число.")
            
            try:
                y = float(y)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля y введено не число.")
            
        if check:
            x_points.append(x)
            y_points.append(y)
            text = '(' + str(x) + ', ' + str(y) + ')'
            self.statusBar().showMessage('Point' + text + ' was added\n')
            self.x_points_entry.setText('')
            self.y_points_entry.setText('')
            self.point = 'Yes'
            self.update()

            '''
            brush = self.QPainter()
            brush.begin(self)
            brush.setPen(Qt.red)
            brush.drawPoint(X + x, Y + y)
            #brush.end()
            '''

        
        print(x_points)
        print(y_points)
    
    def add_point(self, x, y):

    def check_triangle_entry(self):
        check = True
        x1 = self.x1_triangle_entry.text()
        x2 = self.x2_triangle_entry.text()
        x3 = self.x3_triangle_entry.text()

        y1 = self.y1_triangle_entry.text()
        y2 = self.y2_triangle_entry.text()
        y3 = self.y3_triangle_entry.text()
        
        if x1 == '':
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Некорректный ввод!\nВы не ввели координату x1.")
        elif x2 == '':
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Некорректный ввод!\nВы не ввели координату x2.")
        elif x3 == '':
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Некорректный ввод!\nВы не ввели координату x3.")

        elif y1 == '':
            check = False
            QMessageBox.warning(self, "Ошибка!",\
                "Некорректный ввод!\nВы не ввели координату y1.")
        elif y2 == '':
            check = False
            QMessageBox.warning(self, "Ошибка!",\
                "Некорректный ввод!\nВы не ввели координату y2.")
        elif y3 == '':
            check = False
            QMessageBox.warning(self, "Ошибка!",\
                "Некорректный ввод!\nВы не ввели координату y3.")
        else: 
            try:
                x1 = float(x1)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля х1 введено не число.")
            try:
                x2 = float(x2)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля х2 введено не число.")
            try:
                x3 = float(x3)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля х3 введено не число.")
            
            try:
                y1 = float(y1)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля y1 введено не число.")
            try:
                y2 = float(y2)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля y2 введено не число.")
            
            try:
                y3 = float(y3)
            except:
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный ввод!\nДля y3 введено не число.")

        if check:
            xa = (x2 - x1)   # Вычисление координат векторов
            ya = (y2 - y1)      
            xb = (x3 - x2)
            yb = (y3 - y2)
            xc = (x1 - x3)
            yc = (y1 - y3)

            a = sqrt(xa**2 + ya**2)   # Вычисление длин сторон
            b = sqrt(xb**2 + yb**2)
            c = sqrt(xc**2 + yc**2)

            if not (a + b > c and b + c>a and c + a > b):
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный точки!\nТреугольник с такими сторонами не существует.")

        if check:
            x_triangle_points.append(x1)
            x_triangle_points.append(x2)
            x_triangle_points.append(x3)

            y_triangle_points.append(y1)
            y_triangle_points.append(y2)
            y_triangle_points.append(y3)

            self.statusBar().showMessage("Triangle was added")

            self.x1_triangle_entry.setText('')
            self.x2_triangle_entry.setText('')
            self.x3_triangle_entry.setText('')

            self.y1_triangle_entry.setText('')
            self.y2_triangle_entry.setText('')
            self.y3_triangle_entry.setText('')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()


    #sys.exit(app.exec_())
