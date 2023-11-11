# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pseudonym_white.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cupol import starter

pseud = 'Псевдоним' if starter.language == 'rus' else 'Pseudonym'
stones = 'Задать количество камней' if starter.language == 'rus' else 'Set number of stones'
add = 'Задать' if starter.language == 'rus' else 'Set'
many = 'Сколько камней взять?' if starter.language == 'rus' else 'How many stones take?'
take = 'Взять' if starter.language == 'rus' else 'Take'


class Ui_Pseudonym(object):
    def setupUi(self, Pseudonym):
        Pseudonym.setObjectName("Pseudonym")
        Pseudonym.resize(562, 554)
        Pseudonym.setFixedSize(562, 554)
        Pseudonym.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(218, 218, 218, 255));")
        self.stones_label = QtWidgets.QLabel(Pseudonym)
        self.stones_label.setGeometry(QtCore.QRect(10, 34, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stones_label.setFont(font)
        self.stones_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.stones_label.setObjectName("stones_label")
        self.stones = QtWidgets.QSpinBox(Pseudonym)
        self.stones.setGeometry(QtCore.QRect(300, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stones.setFont(font)
        self.stones.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                  "border-radius: 10px;\n"
                                  "border: 3px solid #b7b7b7;\n"
                                  "")
        self.stones.setObjectName("stones")
        self.startButton = QtWidgets.QPushButton(Pseudonym)
        self.startButton.setGeometry(QtCore.QRect(380, 25, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("QPushButton{\n"
                                       "border: 3px solid #b7b7b7;\n"
                                       "border-radius: 10px;\n"
                                       "background-color: none;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #c8c8c8;\n"
                                       "}")
        self.startButton.setObjectName("startButton")
        self.takeInput_label = QtWidgets.QLabel(Pseudonym)
        self.takeInput_label.setGeometry(QtCore.QRect(10, 111, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.takeInput_label.setFont(font)
        self.takeInput_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.takeInput_label.setObjectName("takeInput_label")
        self.takeButton = QtWidgets.QPushButton(Pseudonym)
        self.takeButton.setGeometry(QtCore.QRect(10, 170, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.takeButton.setFont(font)
        self.takeButton.setStyleSheet("QPushButton{\n"
                                      "border: 3px solid #b7b7b7;\n"
                                      "border-radius: 10px;\n"
                                      "background-color: none;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #c8c8c8;\n"
                                      "}")
        self.takeButton.setObjectName("takeButton")
        self.listWidget = QtWidgets.QListWidget(Pseudonym)
        self.listWidget.setGeometry(QtCore.QRect(10, 220, 541, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                      "border-radius: 10px;\n"
                                      "border: 3px solid #b7b7b7;\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        self.resultLabel = QtWidgets.QLabel(Pseudonym)
        self.resultLabel.setGeometry(QtCore.QRect(156, 480, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                       "border-radius: 10px;\n"
                                       "border: 3px solid #b7b7b7;\n"
                                       "")
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.remainLcd = QtWidgets.QLineEdit(Pseudonym)
        self.remainLcd.setGeometry(QtCore.QRect(10, 76, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remainLcd.setFont(font)
        self.remainLcd.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                     "border-radius: 10px;\n"
                                     "border: 3px solid #b7b7b7;\n"
                                     "")
        self.remainLcd.setText("")
        self.remainLcd.setReadOnly(True)
        self.remainLcd.setObjectName("remainLcd")
        self.takeInput = QtWidgets.QLineEdit(Pseudonym)
        self.takeInput.setGeometry(QtCore.QRect(270, 119, 285, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.takeInput.setFont(font)
        self.takeInput.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                     "border-radius: 10px;\n"
                                     "border: 3px solid #b7b7b7;\n"
                                     "")
        self.takeInput.setText("")
        self.takeInput.setObjectName("takeInput")

        self.retranslateUi(Pseudonym)
        QtCore.QMetaObject.connectSlotsByName(Pseudonym)

    def retranslateUi(self, Pseudonym):
        _translate = QtCore.QCoreApplication.translate
        Pseudonym.setWindowTitle(_translate("Pseudonym", f"{pseud}"))
        self.stones_label.setText(_translate("Pseudonym", f"{stones}"))
        self.startButton.setText(_translate("Pseudonym", f"{add}"))
        self.takeInput_label.setText(_translate("Pseudonym", f"{many}"))
        self.takeButton.setText(_translate("Pseudonym", f"{take}"))
