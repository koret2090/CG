# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 990)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 721, 501))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 530, 151, 21))
        self.label.setObjectName("label")
        self.x_centre_circle = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.x_centre_circle.setGeometry(QtCore.QRect(50, 560, 90, 22))
        self.x_centre_circle.setMinimum(-1000.0)
        self.x_centre_circle.setMaximum(2000.0)
        self.x_centre_circle.setObjectName("x_centre_circle")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 563, 21, 16))
        self.label_2.setObjectName("label_2")
        self.y_centre_circle = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.y_centre_circle.setGeometry(QtCore.QRect(180, 560, 90, 22))
        self.y_centre_circle.setMinimum(-1000.0)
        self.y_centre_circle.setMaximum(2000.0)
        self.y_centre_circle.setObjectName("y_centre_circle")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 563, 21, 16))
        self.label_3.setObjectName("label_3")
        self.radius_circle = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.radius_circle.setGeometry(QtCore.QRect(90, 600, 90, 22))
        self.radius_circle.setMinimum(-1000.0)
        self.radius_circle.setMaximum(2000.0)
        self.radius_circle.setObjectName("radius_circle")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 600, 61, 21))
        self.label_5.setObjectName("label_5")
        self.library_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.library_radio.setGeometry(QtCore.QRect(500, 910, 161, 20))
        self.library_radio.setObjectName("library_radio")
        self.build_circle = QtWidgets.QPushButton(self.centralwidget)
        self.build_circle.setGeometry(QtCore.QRect(80, 630, 151, 31))
        self.build_circle.setObjectName("build_circle")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 530, 91, 21))
        self.label_7.setObjectName("label_7")
        self.make_line_black = QtWidgets.QPushButton(self.centralwidget)
        self.make_line_black.setGeometry(QtCore.QRect(500, 560, 93, 28))
        self.make_line_black.setObjectName("make_line_black")
        self.make_line_blue = QtWidgets.QPushButton(self.centralwidget)
        self.make_line_blue.setGeometry(QtCore.QRect(500, 600, 93, 28))
        self.make_line_blue.setObjectName("make_line_blue")
        self.make_line_red = QtWidgets.QPushButton(self.centralwidget)
        self.make_line_red.setGeometry(QtCore.QRect(500, 640, 93, 28))
        self.make_line_red.setObjectName("make_line_red")
        self.make_line_green = QtWidgets.QPushButton(self.centralwidget)
        self.make_line_green.setGeometry(QtCore.QRect(500, 680, 93, 28))
        self.make_line_green.setObjectName("make_line_green")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 530, 91, 21))
        self.label_8.setObjectName("label_8")
        self.make_bg_white = QtWidgets.QPushButton(self.centralwidget)
        self.make_bg_white.setGeometry(QtCore.QRect(610, 560, 93, 28))
        self.make_bg_white.setObjectName("make_bg_white")
        self.make_bg_green = QtWidgets.QPushButton(self.centralwidget)
        self.make_bg_green.setGeometry(QtCore.QRect(610, 680, 93, 28))
        self.make_bg_green.setObjectName("make_bg_green")
        self.make_bg_blue = QtWidgets.QPushButton(self.centralwidget)
        self.make_bg_blue.setGeometry(QtCore.QRect(610, 600, 93, 28))
        self.make_bg_blue.setObjectName("make_bg_blue")
        self.make_bg_red = QtWidgets.QPushButton(self.centralwidget)
        self.make_bg_red.setGeometry(QtCore.QRect(610, 640, 93, 28))
        self.make_bg_red.setObjectName("make_bg_red")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 530, 61, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 560, 21, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.build_circles = QtWidgets.QPushButton(self.centralwidget)
        self.build_circles.setGeometry(QtCore.QRect(310, 660, 161, 31))
        self.build_circles.setObjectName("build_circles")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(500, 760, 181, 21))
        self.label_11.setObjectName("label_11")
        self.make_line_white = QtWidgets.QPushButton(self.centralwidget)
        self.make_line_white.setGeometry(QtCore.QRect(500, 720, 93, 28))
        self.make_line_white.setObjectName("make_line_white")
        self.make_bg_black = QtWidgets.QPushButton(self.centralwidget)
        self.make_bg_black.setGeometry(QtCore.QRect(610, 720, 93, 28))
        self.make_bg_black.setObjectName("make_bg_black")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(310, 560, 51, 21))
        self.label_12.setObjectName("label_12")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(70, 910, 161, 41))
        self.clear_btn.setObjectName("clear_btn")
        self.brezenhem_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.brezenhem_radio.setGeometry(QtCore.QRect(500, 790, 131, 20))
        self.brezenhem_radio.setObjectName("brezenhem_radio")
        self.radius_start_circles = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_start_circles.setGeometry(QtCore.QRect(370, 560, 90, 22))
        self.radius_start_circles.setMinimum(1)
        self.radius_start_circles.setMaximum(1000)
        self.radius_start_circles.setObjectName("radius_start_circles")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 853, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 873, 55, 16))
        self.label_15.setObjectName("label_15")
        self.brush_thickness = QtWidgets.QSpinBox(self.centralwidget)
        self.brush_thickness.setGeometry(QtCore.QRect(110, 863, 90, 22))
        self.brush_thickness.setMinimum(1)
        self.brush_thickness.setMaximum(20)
        self.brush_thickness.setObjectName("brush_thickness")
        self.change_thickness = QtWidgets.QPushButton(self.centralwidget)
        self.change_thickness.setGeometry(QtCore.QRect(210, 860, 61, 28))
        self.change_thickness.setObjectName("change_thickness")
        self.mid_point_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.mid_point_radio.setGeometry(QtCore.QRect(500, 820, 161, 20))
        self.mid_point_radio.setObjectName("mid_point_radio")
        self.canon_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.canon_radio.setGeometry(QtCore.QRect(500, 850, 181, 20))
        self.canon_radio.setObjectName("canon_radio")
        self.parametric_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.parametric_radio.setGeometry(QtCore.QRect(500, 880, 211, 20))
        self.parametric_radio.setObjectName("parametric_radio")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(310, 590, 21, 16))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(310, 590, 51, 21))
        self.label_18.setObjectName("label_18")
        self.radius_step_circles = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_step_circles.setGeometry(QtCore.QRect(370, 590, 90, 22))
        self.radius_step_circles.setMinimum(1)
        self.radius_step_circles.setMaximum(180)
        self.radius_step_circles.setObjectName("radius_step_circles")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 713, 21, 16))
        self.label_4.setObjectName("label_4")
        self.coef_a = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.coef_a.setGeometry(QtCore.QRect(50, 780, 90, 22))
        self.coef_a.setMinimum(-1000.0)
        self.coef_a.setMaximum(2000.0)
        self.coef_a.setObjectName("coef_a")
        self.y_centre_ellipse = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.y_centre_ellipse.setGeometry(QtCore.QRect(180, 710, 90, 22))
        self.y_centre_ellipse.setMinimum(-1000.0)
        self.y_centre_ellipse.setMaximum(2000.0)
        self.y_centre_ellipse.setObjectName("y_centre_ellipse")
        self.build_ellipse = QtWidgets.QPushButton(self.centralwidget)
        self.build_ellipse.setGeometry(QtCore.QRect(80, 810, 151, 31))
        self.build_ellipse.setObjectName("build_ellipse")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 680, 131, 21))
        self.label_6.setObjectName("label_6")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(90, 750, 131, 21))
        self.label_19.setObjectName("label_19")
        self.x_centre_ellipse = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.x_centre_ellipse.setGeometry(QtCore.QRect(50, 710, 90, 22))
        self.x_centre_ellipse.setMinimum(-1000.0)
        self.x_centre_ellipse.setMaximum(2000.0)
        self.x_centre_ellipse.setObjectName("x_centre_ellipse")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(30, 713, 21, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 783, 21, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(160, 783, 21, 16))
        self.label_22.setObjectName("label_22")
        self.coef_b = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.coef_b.setGeometry(QtCore.QRect(180, 780, 90, 22))
        self.coef_b.setMinimum(-1000.0)
        self.coef_b.setMaximum(2000.0)
        self.coef_b.setObjectName("coef_b")
        self.radius_amount_circles = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_amount_circles.setGeometry(QtCore.QRect(370, 620, 90, 22))
        self.radius_amount_circles.setMinimum(1)
        self.radius_amount_circles.setMaximum(180)
        self.radius_amount_circles.setObjectName("radius_amount_circles")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, 620, 21, 16))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 620, 61, 21))
        self.label_16.setObjectName("label_16")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(330, 730, 21, 16))
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(320, 690, 21, 16))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.build_ellipses = QtWidgets.QPushButton(self.centralwidget)
        self.build_ellipses.setGeometry(QtCore.QRect(310, 870, 161, 31))
        self.build_ellipses.setObjectName("build_ellipses")
        self.radius_amount_ellipses = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_amount_ellipses.setGeometry(QtCore.QRect(380, 830, 90, 22))
        self.radius_amount_ellipses.setMinimum(1)
        self.radius_amount_ellipses.setMaximum(180)
        self.radius_amount_ellipses.setObjectName("radius_amount_ellipses")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(300, 820, 21, 16))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(300, 730, 21, 16))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(300, 790, 21, 16))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.radius_step_ellipses = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_step_ellipses.setGeometry(QtCore.QRect(380, 800, 90, 22))
        self.radius_step_ellipses.setMinimum(1)
        self.radius_step_ellipses.setMaximum(180)
        self.radius_step_ellipses.setObjectName("radius_step_ellipses")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(310, 800, 51, 21))
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(310, 830, 61, 21))
        self.label_29.setObjectName("label_29")
        self.radius_start_a_ellipses = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_start_a_ellipses.setGeometry(QtCore.QRect(380, 740, 90, 22))
        self.radius_start_a_ellipses.setMinimum(1)
        self.radius_start_a_ellipses.setMaximum(1000)
        self.radius_start_a_ellipses.setObjectName("radius_start_a_ellipses")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(350, 710, 61, 21))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(310, 740, 61, 21))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(310, 770, 61, 21))
        self.label_32.setObjectName("label_32")
        self.radius_start_b_ellipses = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_start_b_ellipses.setGeometry(QtCore.QRect(380, 770, 90, 22))
        self.radius_start_b_ellipses.setMinimum(1)
        self.radius_start_b_ellipses.setMaximum(1000)
        self.radius_start_b_ellipses.setObjectName("radius_start_b_ellipses")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Центр окружности"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "Радиус"))
        self.library_radio.setText(_translate("MainWindow", "Библиотечный"))
        self.build_circle.setText(_translate("MainWindow", "Построить окр-ть"))
        self.label_7.setText(_translate("MainWindow", "Цвет линии"))
        self.make_line_black.setText(_translate("MainWindow", "Чёрный"))
        self.make_line_blue.setText(_translate("MainWindow", "Синий"))
        self.make_line_red.setText(_translate("MainWindow", "Красный"))
        self.make_line_green.setText(_translate("MainWindow", "Зеленый"))
        self.label_8.setText(_translate("MainWindow", "Цвет фона"))
        self.make_bg_white.setText(_translate("MainWindow", "Белый"))
        self.make_bg_green.setText(_translate("MainWindow", "Зеленый"))
        self.make_bg_blue.setText(_translate("MainWindow", "Синий"))
        self.make_bg_red.setText(_translate("MainWindow", "Красный"))
        self.label_9.setText(_translate("MainWindow", "Спектр "))
        self.build_circles.setText(_translate("MainWindow", "Построить окр-ти"))
        self.label_11.setText(_translate("MainWindow", "Способы"))
        self.make_line_white.setText(_translate("MainWindow", "Белый"))
        self.make_bg_black.setText(_translate("MainWindow", "Чёрный"))
        self.label_12.setText(_translate("MainWindow", "Rнач."))
        self.clear_btn.setText(_translate("MainWindow", "Очистить поле"))
        self.brezenhem_radio.setText(_translate("MainWindow", "Брезенхема"))
        self.label_14.setText(_translate("MainWindow", "Толщина"))
        self.label_15.setText(_translate("MainWindow", "кисти"))
        self.change_thickness.setText(_translate("MainWindow", "Изм."))
        self.mid_point_radio.setText(_translate("MainWindow", "Средней точки"))
        self.canon_radio.setText(_translate("MainWindow", "Каноническое ур-е"))
        self.parametric_radio.setText(_translate("MainWindow", "Параметрическое ур-е"))
        self.label_18.setText(_translate("MainWindow", "Шаг"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.build_ellipse.setText(_translate("MainWindow", "Построить эллипс"))
        self.label_6.setText(_translate("MainWindow", "Центр эллипса"))
        self.label_19.setText(_translate("MainWindow", "Коэффициенты"))
        self.label_20.setText(_translate("MainWindow", "X"))
        self.label_21.setText(_translate("MainWindow", "a"))
        self.label_22.setText(_translate("MainWindow", "b"))
        self.label_16.setText(_translate("MainWindow", "Кол-во"))
        self.build_ellipses.setText(_translate("MainWindow", "Построить эллипсы"))
        self.label_27.setText(_translate("MainWindow", "Шаг"))
        self.label_29.setText(_translate("MainWindow", "Кол-во"))
        self.label_30.setText(_translate("MainWindow", "Спектр "))
        self.label_31.setText(_translate("MainWindow", "Rнач. 1"))
        self.label_32.setText(_translate("MainWindow", "Rнач. 2"))