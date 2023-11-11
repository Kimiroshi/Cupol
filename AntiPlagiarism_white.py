# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AntiPlagiarism_white.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cupol import starter

ant = 'Антиплагиат' if starter.language == 'rus' else 'Antiplagiarism'
text1 = 'Текст 1' if starter.language == 'rus' else 'Text 1'
comp = 'Сравнить' if starter.language == 'rus' else 'Compare'
trigger = 'Порог срабатывания (%):' if starter.language == 'rus' else 'Trigger threshold (%)'
text2 = 'Текст 2' if starter.language == 'rus' else 'Text 2:'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 571)
        MainWindow.setFixedSize(644, 571)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(218, 218, 218, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text1_label = QtWidgets.QLabel(self.centralwidget)
        self.text1_label.setGeometry(QtCore.QRect(10, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text1_label.setFont(font)
        self.text1_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.text1_label.setObjectName("text1_label")
        self.checkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.checkBtn.setGeometry(QtCore.QRect(10, 520, 621, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBtn.setFont(font)
        self.checkBtn.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.checkBtn.setObjectName("checkBtn")
        self.alert_label = QtWidgets.QLabel(self.centralwidget)
        self.alert_label.setGeometry(QtCore.QRect(10, 20, 224, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.alert_label.setFont(font)
        self.alert_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.alert_label.setObjectName("alert_label")
        self.text2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(330, 90, 301, 421))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text2.setFont(font)
        self.text2.setStyleSheet("background: rgba(0,0,0,0);\n"
"border-radius: 10px;\n"
"border: 3px solid #b7b7b7;\n"
"")
        self.text2.setObjectName("text2")
        self.text2_label = QtWidgets.QLabel(self.centralwidget)
        self.text2_label.setGeometry(QtCore.QRect(330, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text2_label.setFont(font)
        self.text2_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.text2_label.setObjectName("text2_label")
        self.text1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 90, 301, 421))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setStyleSheet("background: rgba(0,0,0,0);\n"
"border-radius: 10px;\n"
"border: 3px solid #b7b7b7;\n"
"")
        self.text1.setPlainText("")
        self.text1.setObjectName("text1")
        self.alert_value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.alert_value.setGeometry(QtCore.QRect(237, 21, 401, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.alert_value.setFont(font)
        self.alert_value.setStyleSheet("background: rgba(0,0,0,0);\n"
"border-radius: 5px;\n"
"border: 3px solid #b7b7b7;\n"
"")
        self.alert_value.setMaximum(100.0)
        self.alert_value.setObjectName("alert_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background: none;\n"
"border-radius: 10px;\n"
"border: 3px solid #b7b7b7;\n"
"")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"{ant}"))
        self.text1_label.setText(_translate("MainWindow", f"{text1}"))
        self.checkBtn.setText(_translate("MainWindow", f"{comp}"))
        self.alert_label.setText(_translate("MainWindow", f"{trigger}"))
        self.text2_label.setText(_translate("MainWindow", f"{text2}"))
