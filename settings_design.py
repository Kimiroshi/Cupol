# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cupol import Cupol

starter = Cupol()

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(375, 635)
        Settings.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(218, 218, 218, 255));")
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(154, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("background-color: none")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.account_button = QtWidgets.QPushButton(self.centralwidget)
        self.account_button.setGeometry(QtCore.QRect(8, 10, 51, 51))
        self.account_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.account_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.account_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_button.setIcon(icon)
        self.account_button.setIconSize(QtCore.QSize(37, 37))
        self.account_button.setObjectName("account_button")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(315, 10, 51, 51))
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.home_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QtCore.QSize(50, 50))
        self.home_button.setObjectName("home_button")
        self.theme_choose = QtWidgets.QComboBox(self.centralwidget)
        self.theme_choose.setGeometry(QtCore.QRect(120, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(10)
        self.theme_choose.setFont(font)
        self.theme_choose.setStyleSheet("background-color: none")
        self.theme_choose.setObjectName("theme_choose")
        self.theme_choose.addItem("")
        self.theme_choose.addItem("")
        self.theme_label = QtWidgets.QLabel(self.centralwidget)
        self.theme_label.setGeometry(QtCore.QRect(30, 139, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(14)
        self.theme_label.setFont(font)
        self.theme_label.setStyleSheet("background-color: none")
        self.theme_label.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.theme_label.setObjectName("theme_label")
        self.language_label = QtWidgets.QLabel(self.centralwidget)
        self.language_label.setGeometry(QtCore.QRect(30, 215, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(14)
        self.language_label.setFont(font)
        self.language_label.setStyleSheet("background-color: none")
        self.language_label.setObjectName("language_label")
        self.language_choose = QtWidgets.QComboBox(self.centralwidget)
        self.language_choose.setGeometry(QtCore.QRect(120, 215, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(10)
        self.language_choose.setFont(font)
        self.language_choose.setStyleSheet("background-color: none")
        self.language_choose.setObjectName("language_choose")
        self.language_choose.addItem("")
        self.language_choose.addItem("")
        self.rate_button = QtWidgets.QPushButton(self.centralwidget)
        self.rate_button.setGeometry(QtCore.QRect(298, 285, 51, 51))
        self.rate_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.rate_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rate_button.setIcon(icon2)
        self.rate_button.setIconSize(QtCore.QSize(40, 40))
        self.rate_button.setObjectName("rate_button")
        self.rate_label = QtWidgets.QLabel(self.centralwidget)
        self.rate_label.setGeometry(QtCore.QRect(188, 294, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(14)
        self.rate_label.setFont(font)
        self.rate_label.setStyleSheet("background-color: none")
        self.rate_label.setObjectName("rate_label")
        self.autostart_label = QtWidgets.QLabel(self.centralwidget)
        self.autostart_label.setGeometry(QtCore.QRect(189, 358, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(14)
        self.autostart_label.setFont(font)
        self.autostart_label.setStyleSheet("background-color: none\n"
"")
        self.autostart_label.setObjectName("autostart_label")
        self.autostart = QtWidgets.QCheckBox(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(323, 355, 21, 51))
        self.autostart.setStyleSheet("background-color: none;")
        self.autostart.setText("")
        self.autostart.setIconSize(QtCore.QSize(30, 30))
        self.autostart.setObjectName("autostart")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(70, 480, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(20)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.save_button.setObjectName("save_button")
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        if starter.color == 'black':
            Settings.setStyleSheet(
                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(26, 53, 24, 255), stop:0.663158 rgba(35, 35, 35, 255));;")
            self.home_button.setStyleSheet("QPushButton{\n"
            "border: 3px solid #20603D;\n"
            "border-radius: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #1E5945;\n"
            "}")
            self.account_button.setStyleSheet("QPushButton{\n"
            "border: 3px solid #20603D;\n"
            "border-radius: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #1E5945;\n"
            "}")
            self.rate_button.setStyleSheet("QPushButton{\n"
            "border: 3px solid #20603D;\n"
            "border-radius: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #1E5945;\n"
            "}")
            self.save_button.setStyleSheet("QPushButton{\n"
            "border: 3px solid #20603D;\n"
            "border-radius: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: #A5A5A5;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #1E5945;\n"
            "}")
            self.time_label.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                          "color: #A5A5A5;")
            self.rate_label.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                          "color: #A5A5A5;")
            self.theme_label.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                          "color: #A5A5A5;")
            self.language_label.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                          "color: #A5A5A5;")
            self.autostart_label.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                              "color: #A5A5A5;")
            self.theme_choose.setStyleSheet("QComboBox{\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "border: 3px solid #20603D;\n"
                                            "border-radius: 10px;\n"
                                            "color: #A5A5A5;\n"
                                            "}\n"
                                            "QComboBox:hover{\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "border: 3px solid #20603D;\n"
                                            "border-radius: 10px;\n"
                                            "}")
            self.language_choose.setStyleSheet("QComboBox{\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "border: 3px solid #20603D;\n"
                                            "border-radius: 10px;\n"
                                            "color: #A5A5A5;\n"
                                            "}\n"
                                            "QComboBox:hover{\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "border: 3px solid #20603D;\n"
                                            "border-radius: 10px;\n"
                                            "}")



    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.time_label.setText(_translate("Settings", "0:00"))
        self.theme_choose.setItemText(0, _translate("Settings", "Светлая"))
        self.theme_choose.setItemText(1, _translate("Settings", "Темная"))
        self.theme_label.setText(_translate("Settings", "Тема"))
        self.language_label.setText(_translate("Settings", "Язык"))
        self.language_choose.setItemText(0, _translate("Settings", "Русский"))
        self.language_choose.setItemText(1, _translate("Settings", "Английский"))
        self.rate_label.setText(_translate("Settings", "Оценить"))
        self.autostart_label.setText(_translate("Settings", "Автозапуск"))
        self.save_button.setText(_translate("Settings", "Сохранить"))
