import sys
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint
from cupol import starter

if starter.color == 'black':
    from NimStrikesBack_dark import Ui_Form
else:
    from NimStrikesBack_white import Ui_Form

if starter.language == 'rus':
    win = 'Вы победили, начинаем новую игру'
    lose = 'Вы проиграои, начинаем новую игру'
else:
    win = 'You have won, starting new game'
    lose = 'You have lost, starting new game'

class NimStrikesBack(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        self.ostatok_qlcd.setText(str(self.ostatok))
        self.now_number_qlcd.setText(str(self.number))

    def plus_action(self):
        self.number += self.plus
        self.update()

    def minus_action(self):
        self.number -= self.minus
        self.update()

    def update(self):
        self.ostatok -= 1
        self.result_label.setText("")
        self.ostatok_qlcd.setText(str(self.ostatok))
        self.now_number_qlcd.setText(str(self.number))
        if self.number == 0:
            self.result_label.setText(f"{win}")
            self.number = randint(1, 30)
            self.plus = randint(1, 10)
            self.minus = randint(1, 10)
            self.ostatok = 10
            self.plus_button.setText("+" + str(self.plus))
            self.plus_button.clicked.connect(self.plus_action)
            self.minus_button.setText("-" + str(self.minus))
            self.minus_button.clicked.connect(self.minus_action)
            self.ostatok_qlcd.setText(str(self.ostatok))
            self.now_number_qlcd.setText(str(self.number))
        elif self.ostatok == 0:
            self.result_label.setText(f"{lose}")
            self.number = randint(1, 30)
            self.plus = randint(1, 10)
            self.minus = randint(1, 10)
            self.ostatok = 10
            self.plus_button.setText("+" + str(self.plus))
            self.plus_button.clicked.connect(self.plus_action)
            self.minus_button.setText("-" + str(self.minus))
            self.minus_button.clicked.connect(self.minus_action)
            self.ostatok_qlcd.setText(str(self.ostatok))
            self.now_number_qlcd.setText(str(self.number))


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = NimStrikesBack()
    sx.show()
    sys.exit(sa.exec())
