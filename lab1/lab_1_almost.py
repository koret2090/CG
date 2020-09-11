#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPointF
import design
import random
from random import randint
from math import floor

# НАДО СДЕЛАТЬ КНОПКУ(И) ДЛЯ ОЧИЩЕНИЯ ПОЛЕЙ!!!
#
'''
self.label_9 = QtWidgets.QLabel(self.centralwidget)
self.label_9.setGeometry(QtCore.QRect(640, 460, 21, 21))
'''
X = 20
Y = 10
WIDTH = 800 - 2*X  # 760
HEIGHT = 300 - 2*Y # 280
x_points = [] #array for points' x coordinates
y_points = [] #array for points' y coordinates

x_triangle_points = [] #array for triangle points' x coordinates
y_triangle_points = [] #array for triangle points' y coordinates


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.point = None

        # Для масштаба
        self.scale = 1
        self.max_x = None
        self.min_x = None
        self.max_y = None
        self.min_y = None


        # Для треугольника
        self.triangle = False
        self.x_triangle_centre = None
        self.y_triangle_centre = None
        
        # Для окр-ти
        self.x_circle_centre = None
        self.y_circle_centre = None
        self.radius = None

        # Для касательной
        #self.x_tangent = None
        self.x_tangent_point = None
        self.y_tangent_point = None

        # Для итоговой площади
        self.square = 0
        
        # Для рисунка-результата
        # (треугольник единственный, 
        # не надо описывать доп. переменными)

        # Окружность 
        self.x_result_circle_centre = None
        self.y_result_circle_centre = None
        self.result_radius = None
        self.x1_circle = None
        self.y1_circle = None
        self.x2_circle = None
        self.y2_circle = None
        self.x3_circle = None
        self.y3_circle = None

        # Точка касательной
        self.x_result_tangent_point = None
        self.y_result_tangent_point = None


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
        '''
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(12 + X, 12 + Y, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl.setFont(font)
        self.lbl.setText('text')
        lbl = QtWidgets.QLabel('AAA',self)
        lbl.move(123 + X, 123 + Y)
        '''
        self.dot_lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_4 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_5 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_6 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_7 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_8 = QtWidgets.QLabel(self.centralwidget)
        self.dot_lbl_9 = QtWidgets.QLabel(self.centralwidget)
        
        self.points_table.setReadOnly(1)
        self.triangle_points_table.setReadOnly(1)
        self.add_point_btn.clicked.connect(self.check_points_entry)
        self.add_triangle.clicked.connect(self.check_triangle_entry)
        self.del_point.clicked.connect(self.check_points_deletion)
        self.del_all_points.clicked.connect(self.delete_all_points)
        self.del_triangle.clicked.connect(self.delete_triangle)
        self.task_btn.clicked.connect(self.task)
        self.statusBar()
        self.show()



    def paintEvent(self, event):
        '''
        if self.point == 'Yes':
            print("DIO")
            self.painter = QPainter(self)
            #self.painter.begin(self)
            self.painter.setPen(QPen(Qt.red, 5))

            for i in range(len(x_points)):
                self.painter.drawPoint(X + x_points[i],\
                    Y + y_points[i])
                print("DIO1")
            
            self.painter.end()
            self.point = None
        '''
        self.painter = QPainter(self)
        if (self.square and self.triangle):
            self.find_scale(x_points, x_triangle_points, y_points, y_triangle_points)
            
            
            self.painter.setPen(QPen(Qt.black, 1))

            # Треугольник(основной)
            self.painter.drawPolygon\
                (QPointF(X + x_triangle_points[0], Y + y_triangle_points[0]),\
                    QPointF(X + x_triangle_points[1], Y + y_triangle_points[1]),\
                        QPointF(X + x_triangle_points[2], Y + y_triangle_points[2]))

            # Его точки с подписями
            self.painter.setPen(QPen(Qt.red, 3))
            self.painter.drawPoint(X + x_triangle_points[0], Y + y_triangle_points[0])
            self.painter.drawPoint(X + x_triangle_points[1], Y + y_triangle_points[1])
            self.painter.drawPoint(X + x_triangle_points[2], Y + y_triangle_points[2])

            #self.dot_lbl_1.move(X + x_triangle_points[0], Y + y_triangle_points[0])
            self.dot_lbl_1.setGeometry(QtCore.QRect(X + x_triangle_points[0], Y + y_triangle_points[0], 80, 21))
            text = '(' + str(x_triangle_points[0]) + ', ' + str(y_triangle_points[0]) + ')'
            self.dot_lbl_1.setText(text)
            
            #self.dot_lbl_2.move(X + x_triangle_points[1], Y + y_triangle_points[1])
            self.dot_lbl_2.setGeometry(QtCore.QRect(X + x_triangle_points[1], Y + y_triangle_points[1], 80, 21))
            self.dot_lbl_2.setText('(' + str(x_triangle_points[1]) + ', ' + str(y_triangle_points[1]) + ')')
            
            #self.dot_lbl_3.move(X + x_triangle_points[2], Y + y_triangle_points[2])
            self.dot_lbl_3.setGeometry(QtCore.QRect(X + x_triangle_points[2], Y + y_triangle_points[2], 80, 21))
            self.dot_lbl_3.setText('(' + str(x_triangle_points[2]) + ', ' + str(y_triangle_points[2]) + ')')
            
            # Центр треугольника
            self.painter.drawPoint(self.x_triangle_centre, self.y_triangle_centre)
            #self.dot_lbl_4.move(self.x_triangle_centre, self.y_triangle_centre)
            #self.dot_lbl_4.setText('(' + str(self.x_triangle_centre - X) + ', ' + str(self.y_triangle_centre - Y) + ')')
            
            # Окружность
            self.painter.setPen(QPen(Qt.black, 1))
            self.painter.drawEllipse(QPointF(self.x_result_circle_centre + X,\
                 self.y_result_circle_centre + Y),\
                      self.result_radius, self.result_radius)
            
            self.painter.setPen(QPen(Qt.red, 3))
            self.dot_lbl_7.setGeometry(QtCore.QRect(X + self.x1_circle, Y + self.y1_circle, 80, 21))
            self.dot_lbl_7.setText('(' + str(self.x1_circle) + ', ' + str(self.y1_circle) + ')')
            self.painter.drawPoint(self.x1_circle + X, self.y1_circle + Y)
                
            self.dot_lbl_8.setGeometry(QtCore.QRect(X + self.x2_circle, Y + self.y2_circle, 80, 21))
            self.dot_lbl_8.setText('(' + str(self.x2_circle) + ', ' + str(self.y2_circle) + ')')
            self.painter.drawPoint(self.x2_circle + X, self.y2_circle + Y)

            self.dot_lbl_9.setGeometry(QtCore.QRect(X + self.x3_circle, Y + self.y3_circle, 80, 21))
            self.dot_lbl_9.setText('(' + str(self.x3_circle) + ', ' + str(self.y3_circle) + ')')
            self.painter.drawPoint(self.x3_circle + X, self.y3_circle + Y)
            
            
            # Её центр
            #self.painter.setPen(QPen(Qt.red, 3))
            self.painter.drawPoint(self.x_result_circle_centre + X, \
                self.y_result_circle_centre + Y)
            #self.dot_lbl_5.move(self.x_result_circle_centre + X, self.y_result_circle_centre + Y)
            #self.dot_lbl_5.setText('(' + str(self.x_result_circle_centre) + ', ' + str(self.н_result_circle_centre) + ')')
            
            # Точка касательной
            self.painter.drawPoint(self.x_result_tangent_point + X,\
                self.y_result_tangent_point + Y)
            #self.dot_lbl_6.move(self.x_result_tangent_point + X, self.y_result_tangent_point + Y)
            #self.dot_lbl_6.setText('(' + str(self.x_result_tangent_point) + ', ' + str(self.y_result_tangent_point) + ')')
            
            
            # Треугольник искомый
            self.painter.setPen(QPen(Qt.blue, 2))
            self.painter.drawLine(self.x_triangle_centre,\
                    self.y_triangle_centre, self.x_result_tangent_point + X,\
                        self.y_result_tangent_point + Y)
            
            self.painter.drawLine(self.x_triangle_centre,\
                    self.y_triangle_centre, self.x_result_circle_centre + X,\
                            self.y_result_circle_centre + Y)
            
            self.painter.drawLine(self.x_result_tangent_point + X,\
                    self.y_result_tangent_point + Y, self.x_result_circle_centre + X,\
                            self.y_result_circle_centre + Y)           

        self.update()

        self.painter.end()
    
    def check_points_entry(self):

        #sender = self.sender()
        check = True
        x = self.x_points_entry.text()
        y = self.y_points_entry.text()
        if x == '':
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Некорректный ввод!\nВы не ввели координату x.")
        if y == '':
            check = False
            '''
            msg = QMessageBox()
            msg.setWindowTitle("Внимание!")
            msg.setText("Некорректный ввод!\nВы не ввели координату y.")
            msg.exec()
            '''
            QMessageBox.warning(self, "Ошибка!",\
                "Некорректный ввод!\nВы не ввели координату y.")
        if x != '' and y != '': 
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
            print("CHECKED")
            self.add_point(x, y)
            '''
            brush = self.QPainter()
            brush.begin(self)
            brush.setPen(Qt.red)
            brush.drawPoint(X + x, Y + y)
            #brush.end()
            '''
        '''
        if len(x_points):
            x = x_points[len(x_points) - 1]
            y = y_points[len(y_points) - 1]
            self.delete_point(x, y)
            print(x_points)
            print(y_points)
            self.add_point(x, y)
        '''
        print("X:",x_points)
        print("Y:",y_points)
    
    def add_point(self, x, y):
        x_points.append(x)
        y_points.append(y)
        text = '(' + str(x) + ', ' + str(y) + ')'
        self.statusBar().showMessage('Point' + text + ' was added\n')
        self.x_points_entry.setText('')
        self.y_points_entry.setText('')
        self.point = 'Yes'
        self.points_table.append(text)

        #self.lbl.setText(text)
        
        self.update()

    def check_points_deletion(self):

        #sender = self.sender()
        check = True
        x = self.x_points_entry.text()
        y = self.y_points_entry.text()
        if x == '':
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Некорректный ввод!\nВы не ввели координату x.")
        if y == '':
            check = False
            QMessageBox.warning(self, "Ошибка!",\
                "Некорректный ввод!\nВы не ввели координату y.")
        if x != '' and y != '': 
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
            print("CHECKED")
            self.delete_point(x, y)

    def delete_point(self, x, y):
        x_points.remove(x)
        y_points.remove(y)
        text = '(' + str(x) + ', ' + str(y) + ')'
        self.statusBar().showMessage('Point' + text + ' was deleted\n')
        self.x_points_entry.setText('')
        self.y_points_entry.setText('')
        self.point = 'Yes'
        
        self.points_table.setText('')
        for i in range(len(x_points)):
            text = '(' + str(x_points[i]) + ', ' + str(y_points[i]) + ')'
            self.points_table.append(text)
        
        self.update()
    
    def delete_all_points(self):
        if (x_points == []):
            QMessageBox.warning(self, "Ошибка!", \
                "Нет точек для удаления.")
        else:
            x_points.clear()
            y_points.clear()
            self.points_table.setText('')
            self.statusBar().showMessage("Все точки удалены")
            self.update()
            print(x_points)
            print(y_points)

    def check_triangle_entry(self):
        check = True
        x1 = self.x1_triangle_entry.text()
        x2 = self.x2_triangle_entry.text()
        x3 = self.x3_triangle_entry.text()

        y1 = self.y1_triangle_entry.text()
        y2 = self.y2_triangle_entry.text()
        y3 = self.y3_triangle_entry.text()
        
        if (self.triangle):
            check = False
            QMessageBox.warning(self, "Ошибка!", \
                "Треугольник уже введён!\nУдалите старый треугольник, чтобы ввести новый.")
        elif x1 == '':
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
            # Вычисление координат векторов
            xa = (x2 - x1)   
            ya = (y2 - y1)      
            xb = (x3 - x2)
            yb = (y3 - y2)
            xc = (x1 - x3)
            yc = (y1 - y3)

            # Вычисление длин сторон
            a = sqrt(xa**2 + ya**2)   
            b = sqrt(xb**2 + yb**2)
            c = sqrt(xc**2 + yc**2)

            if not (a + b > c and b + c > a and c + a > b):
                check = False
                QMessageBox.warning(self, "Ошибка!",\
                    "Некорректный точки!\nТреугольник с такими сторонами не существует.")

        if check:
            self.triangle = True
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

            self.triangle_centre(X + x1, Y + y1,\
                X + x2, Y + y2, X + x3, Y + y3)

            for i in range(len(x_triangle_points)):
                text = '(' + str(x_triangle_points[i]) + ', ' + str(y_triangle_points[i]) + ')'
                self.triangle_points_table.append(text)

    def delete_triangle(self):
        if (len(x_triangle_points) != 3):
            QMessageBox.warning(self, "Ошибка!", \
                "Нет треугольника для удаления.")
        else:
            self.triangle = False
            x_triangle_points.clear()
            y_triangle_points.clear()
            self.triangle_points_table.setText('')
            self.statusBar().showMessage("Треугольник удален")
            self.update()

    def triangle_centre(self, x1, y1, x2, y2, x3, y3):
        # через BC и AC  А(x1, y1) B(x2, y2) C(x3, y3)
        x_mid_bc = (x2 + x3) / 2
        y_mid_bc = (y2 + y3) / 2
        
        x_mid_ac = (x1 + x3) / 2
        y_mid_ac = (y1 + y3) / 2

        # Уравнения медиан
        k_bc = (y1 - y_mid_bc) / (x1 - x_mid_bc)
        b_bc = y_mid_bc - k_bc * x_mid_bc

        k_ac = (y2 - y_mid_ac) / (x2 - x_mid_ac)
        b_ac = y_mid_ac - k_ac * x_mid_ac

        # Нахождение координат центра
        self.x_triangle_centre = (b_ac - b_bc) / (k_bc - k_ac)
        self.y_triangle_centre = k_bc * self.x_triangle_centre + b_bc
        
        print(self.x_triangle_centre, self.y_triangle_centre)

        self.x_triangle_centre = (x1 + x2 + x3) / 3 
        self.y_triangle_centre = (y1 + y2 + y3) / 3

        print(self.x_triangle_centre, self.y_triangle_centre)

        
    def cicrcle_centre(self, x1, y1, x2, y2, x3, y3):
        A = x2 - x1
        B = y2 - y1
        C = x3 - x1
        D = y3 - y1
        E = A * (x1 + x2) + B * (y1 + y2)
        F = C * (x1 + x3) + D * (y1 + y3)
        G = 2 * (A * (y3 - y2) - B * (x3 - x2))
        if G != 0:
            self.x_circle_centre = (D * E - B * F) / G
            self.y_circle_centre = (A * F - C * E) / G
            #print("centre: ", self.x_circle_centre, self.y_circle_centre)
            self.radius = (floor(sqrt((self.x_circle_centre - x2)**2 +\
                 ((self.y_circle_centre - y2)**2))) + 1)
            

    def task(self):
        points = len(x_points)
        if (self.triangle and points > 2):
            for i in range(points):
                for j in range(1, points):
                    for k in range(2, points):
                        
                        self.cicrcle_centre(x_points[i], y_points[i],\
                            x_points[j], y_points[j],\
                                x_points[k], y_points[k])
            
                        if (self.radius):
                            self.tangent_point(self.x_triangle_centre,\
                                self.y_triangle_centre, self.x_circle_centre,\
                                    self.y_circle_centre, self.radius)

                            if (self.x_tangent_point != None):
                                self.get_square_and_parameters(\
                                    x_points[i], y_points[i],\
                                        x_points[j], y_points[j],\
                                            x_points[k], y_points[k])
        
        elif (not self.triangle):
            QMessageBox.warning(self, "Ошибка!",\
                    "Не введен треугольник.")
        elif (points < 3):
            QMessageBox.warning(self, "Ошибка!",\
                    "Введено недостаточное кол-во точек (меньше 3)")
        
        if (not self.square):
            QMessageBox.warning(self, "Ошибка!",\
                    "Не удалось вычислить площадь.\nНет подходящих окружностей/треугольника.")
        else:
            answer = "%.3f" % self.square
            QMessageBox.information(self, "Результат",\
                    "Максимальная площадь: " + answer)
        


    def tangent_point(self, x1, y1, x2, y2, r):
        
        centre_to_centre = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if centre_to_centre > r:
            tangent = sqrt(centre_to_centre**2 - r**2) # длина касательной

            d = sqrt((x1-x2)**2 + (y1-y2)**2) # расстояние между центрами
            #a = d / 2
            a = (tangent**2 - self.radius**2 + d**2) / (2 * d)
            h = sqrt(tangent**2 - a**2)
            x = x1 + a * (x2 - x1) / d
            y = y1 + a * (y2 - y1) / d
            self.x_tangent_point = x + (y2 - y1) * h / d
            self.y_tangent_point = y - (x2 - x1) * h / d
            print(self.x_tangent_point, self.y_tangent_point)
        
        else:
            self.x_tangent_point = None
            self.y_tangent_point = None

    def get_square_and_parameters(self, x1, y1, x2, y2, x3, y3):
        # Вычисление координат векторов
        xa = (x2 - x1)   
        ya = (y2 - y1)      
        xb = (x3 - x2)
        yb = (y3 - y2)
        xc = (x1 - x3)
        yc = (y1 - y3)

        # Вычисление длин сторон
        a = sqrt(xa**2 + ya**2)   
        b = sqrt(xb**2 + yb**2)
        c = sqrt(xc**2 + yc**2)

        p = (a + b + c) / 2  # полупериметр
        
        square = sqrt(p * (p - a) * (p - b) * (p - c))
        if square > self.square:
            self.square = square
            
            # Окружность 
            self.x_result_circle_centre = self.x_circle_centre
            self.y_result_circle_centre = self.y_circle_centre
            self.result_radius = self.radius
            self.x1_circle = x1
            self.y1_circle = y1
            self.x2_circle = x2
            self.y2_circle = y2
            self.x3_circle = x3
            self.y3_circle = y3           

            # Точка касательной
            self.x_result_tangent_point = self.x_tangent_point
            self.y_result_tangent_point = self.y_tangent_point

    def find_scale(self, points_x, triangle_points_x, points_y, triangle_points_y):
        points_min_x = min(points_x)
        points_max_x = max(points_x)

        triangle_points_min_x = min(triangle_points_x)
        triangle_points_max_x = max(triangle_points_x)

        minimum_x = min(points_min_x, triangle_points_min_x)
        maximum_x = max(points_max_x, triangle_points_max_x)

        scale_x = WIDTH / (maximum_x - minimum_x)

        points_min_y = min(points_y)
        points_max_y = max(points_y)

        triangle_points_min_y = min(triangle_points_y)
        triangle_points_max_y = max(triangle_points_y)

        minimum_y = min(points_min_y, triangle_points_min_y)
        maximum_y = max(points_max_y, triangle_points_max_y)

        scale_y = HEIGHT / (maximum_y - minimum_y)

        self.scale = min(scale_x, scale_y)
        self.max_x = maximum_x
        self.min_x = minimum_x
        self.max_y = maximum_y
        self.min_y = minimum_y

    def convert_x(self, x):
        return ((x - self.min_x) * self.scale)
    
    def convert_y(self, y):
        return ((self.max_y - y) * self.scale)
                    


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':

    main()


    #sys.exit(app.exec_())
