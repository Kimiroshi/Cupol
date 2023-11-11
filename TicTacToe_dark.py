# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TicTacToe_dark.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cupol import starter

new = 'Новая игра' if starter.language == 'rus' else 'New game'
ttt = 'Крестики-нолики' if starter.language == 'rus' else 'Tic-Tac-Toe'


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(193, 300)
        Form.setFixedSize(193, 300)
        Form.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(26, 53, 24, 255), stop:0.663158 rgba(35, 35, 35, 255));")
        self.X_RadioButton = QtWidgets.QRadioButton(Form)
        self.X_RadioButton.setGeometry(QtCore.QRect(50, 9, 45, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.X_RadioButton.setFont(font)
        self.X_RadioButton.setAutoFillBackground(False)
        self.X_RadioButton.setStyleSheet("background: rgba(0,0,0,0);\n"
                                         "border-radius: 10px;\n"
                                         "border: 3px solid #20603D;\n"
                                         "color: #b7b7b7;\n"
                                         "")
        self.X_RadioButton.setChecked(True)
        self.X_RadioButton.setObjectName("X_RadioButton")
        self.O_RadioButton = QtWidgets.QRadioButton(Form)
        self.O_RadioButton.setGeometry(QtCore.QRect(110, 9, 45, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.O_RadioButton.setFont(font)
        self.O_RadioButton.setStyleSheet("background: rgba(0,0,0,0);\n"
                                         "border-radius: 10px;\n"
                                         "border: 3px solid #20603D;\n"
                                         "color: #b7b7b7;\n"
                                         "")
        self.O_RadioButton.setObjectName("O_RadioButton")
        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(10, 40, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(70, 40, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(130, 40, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(130, 100, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(70, 100, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(10, 100, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(10, 160, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(130, 160, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(70, 160, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton{\n"
                                 "border: 3px solid #20603D;\n"
                                 "border-radius: 10px;\n"
                                 "background-color: none;\n"
                                 "color: #b7b7b7;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #1E5945;\n"
                                 "}")
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setGeometry(QtCore.QRect(10, 220, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("background: rgba(0,0,0,0);\n"
                                        "border-radius: 10px;\n"
                                        "border: 3px solid #20603D;\n"
                                        "color: #b7b7b7;\n"
                                        "")
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.new_game_button = QtWidgets.QPushButton(Form)
        self.new_game_button.setGeometry(QtCore.QRect(40, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_game_button.setFont(font)
        self.new_game_button.setStyleSheet("QPushButton{\n"
                                           "border: 3px solid #20603D;\n"
                                           "border-radius: 10px;\n"
                                           "background-color: none;\n"
                                           "color: #b7b7b7;;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background-color: #1E5945;\n"
                                           "}")
        self.new_game_button.setObjectName("new_game_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", f"{ttt}"))
        self.X_RadioButton.setText(_translate("Form", "X"))
        self.O_RadioButton.setText(_translate("Form", "O"))
        self.new_game_button.setText(_translate("Form", f"{new}"))
