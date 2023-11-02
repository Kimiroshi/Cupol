# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 635)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(218, 218, 218, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.account_button.setIconSize(QtCore.QSize(35, 35))
        self.account_button.setObjectName("account_button")
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
        self.app_1 = QtWidgets.QPushButton(self.centralwidget)
        self.app_1.setGeometry(QtCore.QRect(30, 180, 81, 81))
        self.app_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_1.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_1.setIcon(icon2)
        self.app_1.setIconSize(QtCore.QSize(64, 64))
        self.app_1.setObjectName("app_1")
        self.app_7 = QtWidgets.QPushButton(self.centralwidget)
        self.app_7.setGeometry(QtCore.QRect(150, 380, 81, 81))
        self.app_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_7.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_7.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/tic tac toe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_7.setIcon(icon3)
        self.app_7.setIconSize(QtCore.QSize(70, 90))
        self.app_7.setObjectName("app_7")
        self.app_4 = QtWidgets.QPushButton(self.centralwidget)
        self.app_4.setGeometry(QtCore.QRect(30, 280, 81, 81))
        self.app_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_4.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/game.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_4.setIcon(icon4)
        self.app_4.setIconSize(QtCore.QSize(64, 64))
        self.app_4.setObjectName("app_4")
        self.app_3 = QtWidgets.QPushButton(self.centralwidget)
        self.app_3.setGeometry(QtCore.QRect(270, 180, 81, 81))
        self.app_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_3.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_3.setIcon(icon5)
        self.app_3.setIconSize(QtCore.QSize(64, 64))
        self.app_3.setObjectName("app_3")
        self.app_6 = QtWidgets.QPushButton(self.centralwidget)
        self.app_6.setGeometry(QtCore.QRect(270, 280, 81, 81))
        self.app_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_6.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_6.setIcon(icon6)
        self.app_6.setIconSize(QtCore.QSize(64, 64))
        self.app_6.setObjectName("app_6")
        self.app_2 = QtWidgets.QPushButton(self.centralwidget)
        self.app_2.setGeometry(QtCore.QRect(150, 180, 81, 81))
        self.app_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_2.setWhatsThis("")
        self.app_2.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/calculator_icon-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_2.setIcon(icon7)
        self.app_2.setIconSize(QtCore.QSize(62, 73))
        self.app_2.setObjectName("app_2")
        self.app_5 = QtWidgets.QPushButton(self.centralwidget)
        self.app_5.setGeometry(QtCore.QRect(150, 280, 81, 81))
        self.app_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_5.setStyleSheet("QPushButton{\n"
"border: 3px solid #b7b7b7;\n"
"border-radius: 10px;\n"
"background-color: rgba(0,0,0,0)\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c8c8c8;\n"
"}")
        self.app_5.setText("")
        self.app_5.setIcon(icon4)
        self.app_5.setIconSize(QtCore.QSize(64, 64))
        self.app_5.setObjectName("app_5")
        self.left_button = QtWidgets.QPushButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(120, 550, 51, 41))
        self.left_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_button.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.left_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/left_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_button.setIcon(icon8)
        self.left_button.setObjectName("left_button")
        self.right_button = QtWidgets.QPushButton(self.centralwidget)
        self.right_button.setGeometry(QtCore.QRect(209, 550, 61, 41))
        self.right_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_button.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.right_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/right_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_button.setIcon(icon9)
        self.right_button.setObjectName("right_button")
        self.cur_page = QtWidgets.QLabel(self.centralwidget)
        self.cur_page.setGeometry(QtCore.QRect(190, 560, 16, 16))
        self.cur_page.setStyleSheet("background-color: none")
        self.cur_page.setObjectName("cur_page")
        self.namebg_line = QtWidgets.QLineEdit(self.centralwidget)
        self.namebg_line.setEnabled(True)
        self.namebg_line.setGeometry(QtCore.QRect(130, 89, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(16)
        self.namebg_line.setFont(font)
        self.namebg_line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.namebg_line.setStyleSheet("background: rgba(0,0,0,0);\n"
"border-radius: 10px;\n"
"border: 3px solid #b7b7b7;\n"
"")
        self.namebg_line.setText("")
        self.namebg_line.setMaxLength(32767)
        self.namebg_line.setAlignment(QtCore.Qt.AlignCenter)
        self.namebg_line.setReadOnly(True)
        self.namebg_line.setPlaceholderText("")
        self.namebg_line.setObjectName("namebg_line")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(130, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(18)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("background-color: none")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.account_button.raise_()
        self.settings_button.raise_()
        self.time_label.raise_()
        self.left_button.raise_()
        self.right_button.raise_()
        self.cur_page.raise_()
        self.namebg_line.raise_()
        self.name_label.raise_()
        self.app_1.raise_()
        self.app_2.raise_()
        self.app_3.raise_()
        self.app_4.raise_()
        self.app_5.raise_()
        self.app_6.raise_()
        self.app_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Купол"))
        self.time_label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.time_label.setText(_translate("MainWindow", "0:00"))
        self.app_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>Антиплагиат</p></body></html>"))
        self.app_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Крестики-нолики</p></body></html>"))
        self.app_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ним</p></body></html>"))
        self.app_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Записная книжка</p></body></html>"))
        self.app_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>Планировщик</p></body></html>"))
        self.app_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Калькулятор</span></p></body></html>"))
        self.app_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>Псевдоним</p></body></html>"))
        self.cur_page.setText(_translate("MainWindow", "1"))
        self.name_label.setText(_translate("MainWindow", "Kupol"))
