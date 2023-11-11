# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cupol import starter

log = 'Логин' if starter.language == 'rus' else 'Login'
psw = 'Пароль' if starter.language == 'rus' else 'Password'
leave = 'Выйти из аккаунта' if starter.language == 'rus' else 'Log out'
login = 'Логин:' if starter.language == 'rus' else 'Login:'
password = 'Пароль:' if starter.language == 'rus' else 'Password:'


class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(375, 635)
        AccountWindow.setFixedSize(375, 635)
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(20)
        AccountWindow.setFont(font)
        AccountWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(218, 218, 218, 255));")
        AccountWindow.setIconSize(QtCore.QSize(40, 40))
        AccountWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(AccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(8, 10, 51, 51))
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.home_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QtCore.QSize(45, 45))
        self.home_button.setObjectName("home_button")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(315, 10, 51, 51))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.settings_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setIconSize(QtCore.QSize(40, 40))
        self.settings_button.setObjectName("settings_button")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(154, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("background-color: none")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line.setEnabled(True)
        self.login_line.setGeometry(QtCore.QRect(49, 166, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.login_line.setFont(font)
        self.login_line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.login_line.setStyleSheet("background: rgba(239,237,237,1);\n"
"border-radius: 10px;\n"
"border: 3px solid #b7b7b7;")
        self.login_line.setText("")
        self.login_line.setMaxLength(32767)
        self.login_line.setReadOnly(True)
        self.login_line.setObjectName("login_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setEnabled(True)
        self.password_line.setGeometry(QtCore.QRect(49, 300, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.password_line.setFont(font)
        self.password_line.setAutoFillBackground(False)
        self.password_line.setStyleSheet("background: rgba(239,237,237,1);\n"
"border-radius: 10px;\n"
"border: 3px solid #b7b7b7;\n"
"")
        self.password_line.setText("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_line.setReadOnly(True)
        self.password_line.setObjectName("password_line")
        self.hide_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.hide_password_button.setGeometry(QtCore.QRect(288, 300, 41, 40))
        self.hide_password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide_password_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.hide_password_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_password_button.setIcon(icon2)
        self.hide_password_button.setIconSize(QtCore.QSize(33, 33))
        self.hide_password_button.setObjectName("hide_password_button")
        self.leave_account_button = QtWidgets.QPushButton(self.centralwidget)
        self.leave_account_button.setGeometry(QtCore.QRect(50, 455, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(18)
        self.leave_account_button.setFont(font)
        self.leave_account_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leave_account_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.leave_account_button.setObjectName("leave_account_button")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(50, 132, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(14)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("background-color: none")
        self.login_label.setObjectName("login_label")
        self.password_name = QtWidgets.QLabel(self.centralwidget)
        self.password_name.setGeometry(QtCore.QRect(48, 265, 152, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_name.setFont(font)
        self.password_name.setStyleSheet("background-color: none")
        self.password_name.setObjectName("password_name")
        AccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountWindow)

    def retranslateUi(self, AccountWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountWindow.setWindowTitle(_translate("AccountWindow", "Account"))
        self.time_label.setText(_translate("AccountWindow", "0:00"))
        self.login_line.setPlaceholderText(_translate("AccountWindow", f"{log}"))
        self.password_line.setPlaceholderText(_translate("AccountWindow", f"{psw}"))
        self.leave_account_button.setText(_translate("AccountWindow", f"{leave}"))
        self.login_label.setText(_translate("AccountWindow", f"{login}"))
        self.password_name.setText(_translate("AccountWindow", f"{password}"))

