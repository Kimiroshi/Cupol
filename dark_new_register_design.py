# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dark_new_register_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        RegisterPage.setObjectName("RegisterPage")
        RegisterPage.resize(375, 635)
        RegisterPage.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(26, 53, 24, 255), stop:0.663158 rgba(35, 35, 35, 255));")
        self.centralwidget = QtWidgets.QWidget(RegisterPage)
        self.centralwidget.setObjectName("centralwidget")
        self.login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line.setEnabled(True)
        self.login_line.setGeometry(QtCore.QRect(49, 154, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.login_line.setFont(font)
        self.login_line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.login_line.setStyleSheet("background: #070e0b;\n"
"                                          border-radius: 10px;\n"
"                                          border: 3px solid #20603D;\n"
"                                          color: white")
        self.login_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.login_line.setInputMask("")
        self.login_line.setText("")
        self.login_line.setMaxLength(32767)
        self.login_line.setReadOnly(False)
        self.login_line.setObjectName("login_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setEnabled(True)
        self.password_line.setGeometry(QtCore.QRect(49, 236, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.password_line.setFont(font)
        self.password_line.setAutoFillBackground(False)
        self.password_line.setStyleSheet("background: #070e0b;\n"
"                                          border-radius: 10px;\n"
"                                          border: 3px solid #20603D;\n"
"                                          color: white")
        self.password_line.setText("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_line.setReadOnly(False)
        self.password_line.setObjectName("password_line")
        self.hide_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.hide_password_button.setGeometry(QtCore.QRect(288, 236, 41, 40))
        self.hide_password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide_password_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #20603D;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #1E5945;\n"
"}")
        self.hide_password_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_password_button.setIcon(icon)
        self.hide_password_button.setIconSize(QtCore.QSize(33, 33))
        self.hide_password_button.setObjectName("hide_password_button")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(37, 58, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("background-color: none;\n"
"color: gray")
        self.welcome_label.setObjectName("welcome_label")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(49, 516, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(15)
        self.register_button.setFont(font)
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #20603D;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"color: gray\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #1E5945;\n"
"}")
        self.register_button.setObjectName("register_button")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(49, 417, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(18)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #20603D;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"color: gray\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #1E5945;\n"
"}")
        self.login_button.setObjectName("login_button")
        self.or_label = QtWidgets.QLabel(self.centralwidget)
        self.or_label.setGeometry(QtCore.QRect(170, 469, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.or_label.setFont(font)
        self.or_label.setStyleSheet("background-color: rgba(0,0,0,0)\n"
"")
        self.or_label.setObjectName("or_label")
        self.remember_me_label = QtWidgets.QLineEdit(self.centralwidget)
        self.remember_me_label.setEnabled(True)
        self.remember_me_label.setGeometry(QtCore.QRect(49, 320, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.remember_me_label.setFont(font)
        self.remember_me_label.setAutoFillBackground(False)
        self.remember_me_label.setStyleSheet("background: #070e0b;\n"
"                                          border-radius: 10px;\n"
"                                          border: 3px solid #20603D;\n"
"                                          color: white")
        self.remember_me_label.setText("")
        self.remember_me_label.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.remember_me_label.setReadOnly(True)
        self.remember_me_label.setObjectName("remember_me_label")
        self.remember_me_button = QtWidgets.QPushButton(self.centralwidget)
        self.remember_me_button.setGeometry(QtCore.QRect(288, 320, 41, 40))
        self.remember_me_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remember_me_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #20603D;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #1E5945;\n"
"}")
        self.remember_me_button.setText("")
        self.remember_me_button.setIconSize(QtCore.QSize(33, 33))
        self.remember_me_button.setObjectName("remember_me_button")
        RegisterPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterPage)
        QtCore.QMetaObject.connectSlotsByName(RegisterPage)

    def retranslateUi(self, RegisterPage):
        _translate = QtCore.QCoreApplication.translate
        RegisterPage.setWindowTitle(_translate("RegisterPage", "Register"))
        self.login_line.setPlaceholderText(_translate("RegisterPage", "Логин"))
        self.password_line.setPlaceholderText(_translate("RegisterPage", "Пароль"))
        self.welcome_label.setText(_translate("RegisterPage", "Добро пожаловать в Cupol"))
        self.register_button.setText(_translate("RegisterPage", "Зарегестрироваться"))
        self.login_button.setText(_translate("RegisterPage", "Войти"))
        self.or_label.setText(_translate("RegisterPage", "или"))
        self.remember_me_label.setPlaceholderText(_translate("RegisterPage", "Запомнить меня"))
