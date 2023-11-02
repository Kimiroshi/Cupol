# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dark_rate_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RateWindow(object):
    def setupUi(self, RateWindow):
        RateWindow.setObjectName("RateWindow")
        RateWindow.resize(561, 190)
        RateWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(26, 53, 24, 255), stop:0.663158 rgba(35, 35, 35, 255));")
        self.centralwidget = QtWidgets.QWidget(RateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.star1 = QtWidgets.QPushButton(self.centralwidget)
        self.star1.setGeometry(QtCore.QRect(50, 70, 71, 71))
        self.star1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.star1.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.star1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/rate_star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.star1.setIcon(icon)
        self.star1.setIconSize(QtCore.QSize(64, 64))
        self.star1.setObjectName("star1")
        self.star2 = QtWidgets.QPushButton(self.centralwidget)
        self.star2.setGeometry(QtCore.QRect(150, 70, 71, 71))
        self.star2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.star2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.star2.setText("")
        self.star2.setIcon(icon)
        self.star2.setIconSize(QtCore.QSize(64, 64))
        self.star2.setObjectName("star2")
        self.star4 = QtWidgets.QPushButton(self.centralwidget)
        self.star4.setGeometry(QtCore.QRect(350, 70, 71, 71))
        self.star4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.star4.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.star4.setText("")
        self.star4.setIcon(icon)
        self.star4.setIconSize(QtCore.QSize(64, 64))
        self.star4.setObjectName("star4")
        self.star3 = QtWidgets.QPushButton(self.centralwidget)
        self.star3.setGeometry(QtCore.QRect(250, 70, 71, 71))
        self.star3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.star3.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.star3.setText("")
        self.star3.setIcon(icon)
        self.star3.setIconSize(QtCore.QSize(64, 64))
        self.star3.setObjectName("star3")
        self.star5 = QtWidgets.QPushButton(self.centralwidget)
        self.star5.setGeometry(QtCore.QRect(450, 70, 71, 71))
        self.star5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.star5.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.star5.setText("")
        self.star5.setIcon(icon)
        self.star5.setIconSize(QtCore.QSize(64, 64))
        self.star5.setObjectName("star5")
        self.msg_label = QtWidgets.QLabel(self.centralwidget)
        self.msg_label.setGeometry(QtCore.QRect(154, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(18)
        self.msg_label.setFont(font)
        self.msg_label.setStyleSheet("background-color: none;\n"
"color: gray")
        self.msg_label.setObjectName("msg_label")
        RateWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RateWindow)
        QtCore.QMetaObject.connectSlotsByName(RateWindow)

    def retranslateUi(self, RateWindow):
        _translate = QtCore.QCoreApplication.translate
        RateWindow.setWindowTitle(_translate("RateWindow", "MainWindow"))
        self.msg_label.setText(_translate("RateWindow", "Поставьте оценку"))
