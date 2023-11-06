import sys
from math import factorial
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from cupol import starter
if starter.color == "black":
    interface = "calc_dark.ui"
else:
    interface = "calc.ui"


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface, self)
        self.initUI()

    def initUI(self):
        self.second_label = []
        self.first_label = "0"
        self.flag = 0

        self.main_label = self.table

        self.number_buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7,
                               self.btn8, self.btn9]
        for i in range(10):
            self.number_buttons[i].clicked.connect(self.number)

        self.clear_button = self.btn_clear
        self.clear_button.clicked.connect(self.c)

        self.divide_button = self.btn_div
        self.divide_button.clicked.connect(self.action)

        self.multiply_button = self.btn_mult
        self.multiply_button.clicked.connect(self.action)

        self.substract_button = self.btn_minus
        self.substract_button.clicked.connect(self.action)

        self.add_button = self.btn_plus
        self.add_button.clicked.connect(self.action)

        self.float_point_button = self.btn_dot
        self.float_point_button.clicked.connect(self.dot)

        self.equals_button = self.btn_eq
        self.equals_button.clicked.connect(self.equals)

        self.btn_pow.clicked.connect(self.pow)

        self.btn_sqrt.clicked.connect(self.sqrt)

        self.btn_fact.clicked.connect(self.fact)

    def update(self):
        self.main_label.display(self.first_label)

    def number(self):
        if self.first_label == "0" or self.flag == 1:
            self.first_label = ""
        self.first_label += self.sender().text()
        self.flag = 0
        self.update()

    def c(self):
        self.first_label = "0"
        self.second_label = []
        self.flag = 0
        self.update()

    def action(self):
        if len(self.first_label) > 30:
            self.first_label = f"{float(self.first_label):.2E}"
        if "." in self.first_label:
            self.second_label = [float(self.first_label), self.sender().text()]
        else:
            self.second_label = [int(self.first_label), self.sender().text()]
        self.flag = 1
        self.update()

    def dot(self):
        if "." not in self.first_label:
            self.first_label += self.sender().text()
        self.update()

    def equals(self):
        if not (self.second_label[1] == "/" and int(float(self.first_label)) == 0):
            if len(str(eval(f"{self.second_label[0]} {self.second_label[1]} {self.first_label}"))) > 11:
                self.first_label = f"{eval(f'{self.second_label[0]} {self.second_label[1]} {self.first_label}'):.2E}"
            else:
                self.first_label = str(eval(f"{self.second_label[0]} {self.second_label[1]} {self.first_label}"))
            self.second_label = []
            self.update()
        else:
            self.main_label.display("Error")

    def pow(self):
        if len(self.first_label) > 30:
            self.first_label = f"{float(self.first_label):.2E}"
        if "." in self.first_label:
            self.second_label = [float(self.first_label), "**"]
        else:
            self.second_label = [int(self.first_label), "**"]
        self.flag = 1
        self.update()

    def sqrt(self):
        if int(float(self.first_label)) < 0:
            self.first_label = "Error"
        elif "." in self.first_label:
            self.first_label = str(round(float(self.first_label) ** 0.5, 1))
            if float(self.first_label) // 1 == float(self.first_label):
                self.first_label = str(int(float(self.first_label)))
        else:
            self.first_label = str(round(int(self.first_label) ** 0.5, 1))
            if float(self.first_label) // 1 == float(self.first_label):
                self.first_label = str(int(float(self.first_label)))
        self.update()

    def fact(self):
        if "." in self.first_label or int(float(self.first_label)) < 0:
            self.first_label = "Error"
        else:
            self.first_label = str(factorial(int(self.first_label)))
        self.update()


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = Calculator()
    sx.show()
    sys.exit(sa.exec())
