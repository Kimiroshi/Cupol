# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyNotes_white.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cupol import starter

pb = 'Телефонная книжка' if starter.language == 'rus' else 'Phone book'
name = 'Имя:' if starter.language == 'rus' else 'Name:'
phone = 'Телефон:' if starter.language == 'rus' else 'Phone:'
add = 'Добавить' if starter.language == 'rus' else 'Add'


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(334, 535)
        Form.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(218, 218, 218, 255));")
        self.contactName_label = QtWidgets.QLabel(Form)
        self.contactName_label.setGeometry(QtCore.QRect(10, 10, 66, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contactName_label.setFont(font)
        self.contactName_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.contactName_label.setObjectName("contactName_label")
        self.contactNumber_label = QtWidgets.QLabel(Form)
        self.contactNumber_label.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contactNumber_label.setFont(font)
        self.contactNumber_label.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.contactNumber_label.setObjectName("contactNumber_label")
        self.contactName = QtWidgets.QLineEdit(Form)
        self.contactName.setGeometry(QtCore.QRect(80, 12, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.contactName.setFont(font)
        self.contactName.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                       "border-radius: 10px;\n"
                                       "border: 3px solid #b7b7b7;\n"
                                       "")
        self.contactName.setText("")
        self.contactName.setObjectName("contactName")
        self.contactNumber = QtWidgets.QLineEdit(Form)
        self.contactNumber.setGeometry(QtCore.QRect(115, 52, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.contactNumber.setFont(font)
        self.contactNumber.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                         "border-radius: 10px;\n"
                                         "border: 3px solid #b7b7b7;\n"
                                         "")
        self.contactNumber.setText("")
        self.contactNumber.setObjectName("contactNumber")
        self.addContactBtn = QtWidgets.QPushButton(Form)
        self.addContactBtn.setGeometry(QtCore.QRect(10, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addContactBtn.setFont(font)
        self.addContactBtn.setStyleSheet("QPushButton{\n"
                                         "border: 3px solid #b7b7b7;\n"
                                         "border-radius: 10px;\n"
                                         "background-color: none;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #c8c8c8;\n"
                                         "}")
        self.addContactBtn.setObjectName("addContactBtn")
        self.contactList = QtWidgets.QListWidget(Form)
        self.contactList.setGeometry(QtCore.QRect(10, 140, 311, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contactList.setFont(font)
        self.contactList.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                       "border-radius: 10px;\n"
                                       "border: 3px solid #b7b7b7;\n"
                                       "")
        self.contactList.setObjectName("contactList")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", f"{pb}"))
        self.contactName_label.setText(_translate("Form", f"{name}"))
        self.contactNumber_label.setText(_translate("Form", f"{phone}"))
        self.addContactBtn.setText(_translate("Form", f"{add}"))
