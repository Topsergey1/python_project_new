# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator_My_ingenern.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 479)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_ac = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ac.setGeometry(QtCore.QRect(250, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_ac.setFont(font)
        self.pushButton_ac.setStyleSheet("color: #f44336;")
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.pushButton_ce = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ce.setGeometry(QtCore.QRect(330, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_ce.setFont(font)
        self.pushButton_ce.setStyleSheet("color: #f44336;")
        self.pushButton_ce.setObjectName("pushButton_ce")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(410, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_mr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mr.setGeometry(QtCore.QRect(330, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mr.setFont(font)
        self.pushButton_mr.setObjectName("pushButton_mr")
        self.pushButton_mm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mm.setGeometry(QtCore.QRect(410, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mm.setFont(font)
        self.pushButton_mm.setObjectName("pushButton_mm")
        self.pushButton_mp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mp.setGeometry(QtCore.QRect(490, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mp.setFont(font)
        self.pushButton_mp.setObjectName("pushButton_mp")
        self.pushButton_pm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pm.setGeometry(QtCore.QRect(170, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_pm.setFont(font)
        self.pushButton_pm.setObjectName("pushButton_pm")
        self.pushButton_n7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n7.setGeometry(QtCore.QRect(250, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.pushButton_n9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n9.setGeometry(QtCore.QRect(410, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.pushButton_n8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n8.setGeometry(QtCore.QRect(330, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.pushButton_n4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n4.setGeometry(QtCore.QRect(250, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(490, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_n6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n6.setGeometry(QtCore.QRect(410, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.pushButton_n5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n5.setGeometry(QtCore.QRect(330, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(490, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_n1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n1.setGeometry(QtCore.QRect(250, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(490, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_n3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n3.setGeometry(QtCore.QRect(410, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.pushButton_n2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n2.setGeometry(QtCore.QRect(330, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.pushButton_n0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n0.setGeometry(QtCore.QRect(330, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.pushButton_eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eq.setGeometry(QtCore.QRect(490, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.pushButton_point = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_point.setGeometry(QtCore.QRect(250, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_n00 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n00.setGeometry(QtCore.QRect(410, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_n00.setFont(font)
        self.pushButton_n00.setObjectName("pushButton_n00")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(490, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 551, 87))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_mc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mc.setGeometry(QtCore.QRect(250, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mc.setFont(font)
        self.pushButton_mc.setObjectName("pushButton_mc")
        self.pushButton_1divx_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1divx_2.setGeometry(QtCore.QRect(90, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1divx_2.setFont(font)
        self.pushButton_1divx_2.setObjectName("pushButton_1divx_2")
        self.pushButton_pc_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pc_2.setGeometry(QtCore.QRect(10, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_pc_2.setFont(font)
        self.pushButton_pc_2.setText("")
        self.pushButton_pc_2.setObjectName("pushButton_pc_2")
        self.pushButton_sqr_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_5.setGeometry(QtCore.QRect(10, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_5.setFont(font)
        self.pushButton_sqr_5.setObjectName("pushButton_sqr_5")
        self.pushButton_1divx_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1divx_3.setGeometry(QtCore.QRect(170, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1divx_3.setFont(font)
        self.pushButton_1divx_3.setObjectName("pushButton_1divx_3")
        self.pushButton_pc_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pc_3.setGeometry(QtCore.QRect(170, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_pc_3.setFont(font)
        self.pushButton_pc_3.setObjectName("pushButton_pc_3")
        self.pushButton_sqr_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_6.setGeometry(QtCore.QRect(90, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_6.setFont(font)
        self.pushButton_sqr_6.setObjectName("pushButton_sqr_6")
        self.pushButton_sqr_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_7.setGeometry(QtCore.QRect(90, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_7.setFont(font)
        self.pushButton_sqr_7.setObjectName("pushButton_sqr_7")
        self.pushButton_1divx_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1divx_4.setGeometry(QtCore.QRect(90, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1divx_4.setFont(font)
        self.pushButton_1divx_4.setObjectName("pushButton_1divx_4")
        self.pushButton_pc_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pc_4.setGeometry(QtCore.QRect(10, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_pc_4.setFont(font)
        self.pushButton_pc_4.setObjectName("pushButton_pc_4")
        self.pushButton_sqr_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_8.setGeometry(QtCore.QRect(10, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_8.setFont(font)
        self.pushButton_sqr_8.setObjectName("pushButton_sqr_8")
        self.pushButton_sqr_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_9.setGeometry(QtCore.QRect(10, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_9.setFont(font)
        self.pushButton_sqr_9.setObjectName("pushButton_sqr_9")
        self.pushButton_1divx_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1divx_5.setGeometry(QtCore.QRect(170, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1divx_5.setFont(font)
        self.pushButton_1divx_5.setObjectName("pushButton_1divx_5")
        self.pushButton_pc_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pc_5.setGeometry(QtCore.QRect(170, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_pc_5.setFont(font)
        self.pushButton_pc_5.setObjectName("pushButton_pc_5")
        self.pushButton_sqr_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_10.setGeometry(QtCore.QRect(90, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_10.setFont(font)
        self.pushButton_sqr_10.setObjectName("pushButton_sqr_10")
        self.pushButton_sqr_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_11.setGeometry(QtCore.QRect(10, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_11.setFont(font)
        self.pushButton_sqr_11.setObjectName("pushButton_sqr_11")
        self.pushButton_sqr_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr_12.setGeometry(QtCore.QRect(90, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqr_12.setFont(font)
        self.pushButton_sqr_12.setObjectName("pushButton_sqr_12")
        self.pushButton_1divx_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1divx_6.setGeometry(QtCore.QRect(170, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1divx_6.setFont(font)
        self.pushButton_1divx_6.setObjectName("pushButton_1divx_6")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 110, 101, 17))
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 110, 101, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(250, 110, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ac.setText(_translate("MainWindow", "AC"))
        self.pushButton_ce.setText(_translate("MainWindow", "CE/C"))
        self.pushButton_del.setText(_translate("MainWindow", "→"))
        self.pushButton_mr.setText(_translate("MainWindow", "MR"))
        self.pushButton_mm.setText(_translate("MainWindow", "M-"))
        self.pushButton_mp.setText(_translate("MainWindow", "M+"))
        self.pushButton_pm.setText(_translate("MainWindow", "+ / -"))
        self.pushButton_n7.setText(_translate("MainWindow", "7"))
        self.pushButton_n9.setText(_translate("MainWindow", "9"))
        self.pushButton_n8.setText(_translate("MainWindow", "8"))
        self.pushButton_n4.setText(_translate("MainWindow", "4"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_n6.setText(_translate("MainWindow", "6"))
        self.pushButton_n5.setText(_translate("MainWindow", "5"))
        self.pushButton_mul.setText(_translate("MainWindow", "x"))
        self.pushButton_n1.setText(_translate("MainWindow", "1"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_n3.setText(_translate("MainWindow", "3"))
        self.pushButton_n2.setText(_translate("MainWindow", "2"))
        self.pushButton_n0.setText(_translate("MainWindow", "0"))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_n00.setText(_translate("MainWindow", "00"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_mc.setText(_translate("MainWindow", "MC"))
        self.pushButton_1divx_2.setText(_translate("MainWindow", "1/x"))
        self.pushButton_sqr_5.setText(_translate("MainWindow", "x\'2"))
        self.pushButton_1divx_3.setText(_translate("MainWindow", "x\'n"))
        self.pushButton_pc_3.setText(_translate("MainWindow", "x!"))
        self.pushButton_sqr_6.setText(_translate("MainWindow", "x\'3"))
        self.pushButton_sqr_7.setText(_translate("MainWindow", "%"))
        self.pushButton_1divx_4.setText(_translate("MainWindow", "log"))
        self.pushButton_pc_4.setText(_translate("MainWindow", "ln"))
        self.pushButton_sqr_8.setText(_translate("MainWindow", "e\'n"))
        self.pushButton_sqr_9.setText(_translate("MainWindow", "sin"))
        self.pushButton_1divx_5.setText(_translate("MainWindow", "tn"))
        self.pushButton_pc_5.setText(_translate("MainWindow", "Pi"))
        self.pushButton_sqr_10.setText(_translate("MainWindow", "cos"))
        self.pushButton_sqr_11.setText(_translate("MainWindow", "sin-1"))
        self.pushButton_sqr_12.setText(_translate("MainWindow", "cos-1"))
        self.pushButton_1divx_6.setText(_translate("MainWindow", "tn-1"))
        self.radioButton.setText(_translate("MainWindow", "Градусы"))
        self.radioButton_2.setText(_translate("MainWindow", "Радианы"))
        self.radioButton_3.setText(_translate("MainWindow", "Грады"))
