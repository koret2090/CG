# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 815)
        font = QtGui.QFont()
        font.setPointSize(6)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.add_point_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_point_btn.setGeometry(QtCore.QRect(30, 430, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_point_btn.setFont(font)
        self.add_point_btn.setObjectName("add_point_btn")
        self.x_points_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.x_points_entry.setGeometry(QtCore.QRect(40, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x_points_entry.setFont(font)
        self.x_points_entry.setObjectName("x_points_entry")
        self.y_points_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.y_points_entry.setGeometry(QtCore.QRect(150, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y_points_entry.setFont(font)
        self.y_points_entry.setObjectName("y_points_entry")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 380, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 380, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.del_point = QtWidgets.QPushButton(self.centralwidget)
        self.del_point.setGeometry(QtCore.QRect(30, 470, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_point.setFont(font)
        self.del_point.setObjectName("del_point")
        self.del_all_points = QtWidgets.QPushButton(self.centralwidget)
        self.del_all_points.setGeometry(QtCore.QRect(30, 510, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_all_points.setFont(font)
        self.del_all_points.setObjectName("del_all_points")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 339, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.x1_triangle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.x1_triangle_entry.setGeometry(QtCore.QRect(550, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x1_triangle_entry.setFont(font)
        self.x1_triangle_entry.setObjectName("x1_triangle_entry")
        self.y1_triangle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.y1_triangle_entry.setGeometry(QtCore.QRect(660, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y1_triangle_entry.setFont(font)
        self.y1_triangle_entry.setObjectName("y1_triangle_entry")
        self.x2_triangle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.x2_triangle_entry.setGeometry(QtCore.QRect(550, 410, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x2_triangle_entry.setFont(font)
        self.x2_triangle_entry.setObjectName("x2_triangle_entry")
        self.y2_triangle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.y2_triangle_entry.setGeometry(QtCore.QRect(660, 410, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y2_triangle_entry.setFont(font)
        self.y2_triangle_entry.setObjectName("y2_triangle_entry")
        self.x3_triangle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.x3_triangle_entry.setGeometry(QtCore.QRect(550, 450, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x3_triangle_entry.setFont(font)
        self.x3_triangle_entry.setObjectName("x3_triangle_entry")
        self.y3_triangle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.y3_triangle_entry.setGeometry(QtCore.QRect(660, 450, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y3_triangle_entry.setFont(font)
        self.y3_triangle_entry.setObjectName("y3_triangle_entry")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 380, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 420, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 460, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 380, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(640, 420, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 460, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(450, 380, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 340, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(450, 420, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 460, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.add_triangle = QtWidgets.QPushButton(self.centralwidget)
        self.add_triangle.setGeometry(QtCore.QRect(520, 500, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_triangle.setFont(font)
        self.add_triangle.setObjectName("add_triangle")
        self.del_triangle = QtWidgets.QPushButton(self.centralwidget)
        self.del_triangle.setGeometry(QtCore.QRect(640, 500, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_triangle.setFont(font)
        self.del_triangle.setObjectName("del_triangle")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 310, 761, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 10, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(770, 10, 20, 311))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 0, 761, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.points_table = QtWidgets.QTextEdit(self.centralwidget)
        self.points_table.setEnabled(True)
        self.points_table.setGeometry(QtCore.QRect(250, 370, 161, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.points_table.setFont(font)
        self.points_table.setObjectName("points_table")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(260, 340, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.triangle_points_table = QtWidgets.QTextEdit(self.centralwidget)
        self.triangle_points_table.setEnabled(True)
        self.triangle_points_table.setGeometry(QtCore.QRect(490, 580, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.triangle_points_table.setFont(font)
        self.triangle_points_table.setObjectName("triangle_points_table")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(540, 550, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.task_btn.setGeometry(QtCore.QRect(20, 630, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.task_btn.setFont(font)
        self.task_btn.setObjectName("task_btn")
        self.task_conditions = QtWidgets.QTextEdit(self.centralwidget)
        self.task_conditions.setEnabled(True)
        self.task_conditions.setGeometry(QtCore.QRect(20, 710, 761, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.task_conditions.setFont(font)
        self.task_conditions.setObjectName("task_conditions")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_point_btn.setText(_translate("MainWindow", "Add "))
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.del_point.setText(_translate("MainWindow", "Delete"))
        self.del_all_points.setText(_translate("MainWindow", "Delete all points"))
        self.label_3.setText(_translate("MainWindow", "Triangle\'s coordinates"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "X:"))
        self.label_6.setText(_translate("MainWindow", "X:"))
        self.label_7.setText(_translate("MainWindow", "Y:"))
        self.label_8.setText(_translate("MainWindow", "Y:"))
        self.label_9.setText(_translate("MainWindow", "Y:"))
        self.label_10.setText(_translate("MainWindow", "Point 1"))
        self.label_11.setText(_translate("MainWindow", "Points"))
        self.label_12.setText(_translate("MainWindow", "Point 2"))
        self.label_13.setText(_translate("MainWindow", "Point 3"))
        self.add_triangle.setText(_translate("MainWindow", "Add "))
        self.del_triangle.setText(_translate("MainWindow", "Delete"))
        self.label_14.setText(_translate("MainWindow", "Entered Points"))
        self.label_15.setText(_translate("MainWindow", "Triangle\'s points"))
        self.task_btn.setText(_translate("MainWindow", "Do task"))
