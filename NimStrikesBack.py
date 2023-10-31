import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('NimStrikesBack.ui', self)
        self.initUI()

    def initUI(self):
        self.number = randint(1, 30)
        self.plus = randint(1, 10)
        self.minus = randint(1, 10)
        self.ostatok = 10

        self.plus_button.setText("+" + str(self.plus))
        self.plus_button.clicked.connect(self.plus_action)
        self.minus_button.setText("-" + str(self.minus))
        self.minus_button.clicked.connect(self.minus_action)

        self.ostatok_qlcd.display(self.ostatok)
        self.now_number_qlcd.display(self.number)

    def plus_action(self):
        self.number += self.plus
        self.update()

    def minus_action(self):
        self.number -= self.minus
        self.update()

    def update(self):
        self.ostatok -= 1
        self.result_label.setText("")
        self.ostatok_qlcd.display(self.ostatok)
        self.now_number_qlcd.display(self.number)
        if self.number == 0:
            self.result_label.setText("Вы победили, начинаем новую игру")
            self.number = randint(1, 30)
            self.plus = randint(1, 10)
            self.minus = randint(1, 10)
            self.ostatok = 10
            self.plus_button.setText("+" + str(self.plus))
            self.plus_button.clicked.connect(self.plus_action)
            self.minus_button.setText("-" + str(self.minus))
            self.minus_button.clicked.connect(self.minus_action)
            self.ostatok_qlcd.display(self.ostatok)
            self.now_number_qlcd.display(self.number)
        elif self.ostatok == 0:
            self.result_label.setText("Вы проиграли, начинаем новую игру")
            self.number = randint(1, 30)
            self.plus = randint(1, 10)
            self.minus = randint(1, 10)
            self.ostatok = 10
            self.plus_button.setText("+" + str(self.plus))
            self.plus_button.clicked.connect(self.plus_action)
            self.minus_button.setText("-" + str(self.minus))
            self.minus_button.clicked.connect(self.minus_action)
            self.ostatok_qlcd.display(self.ostatok)
            self.now_number_qlcd.display(self.number)


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = NimStrikesBack()
    sx.show()
    sys.exit(sa.exec())
