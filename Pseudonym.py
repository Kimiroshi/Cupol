import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from cupol import starter

if starter.color == 'black':
    from Pseudonym_dark import Ui_Pseudonym
else:
    from Pseudonym_white import Ui_Pseudonym

if starter.language == 'rus':
    win = 'Победа пользователя!'
    take = 'Игрок взял'
    pctake = 'Компьютер взял'
    pcwin = 'Победа компьютера!'
    err = 'Ошибка:'
    text = 'Похоже вы ввели некорректное число'
else:
    win = 'User win!'
    take = 'Player took'
    pctake = 'Computer took'
    pcwin = 'Computer victory!'
    err = 'Error:'
    text = 'It looks like you entered an incorrect number'


class Pseudonym(QWidget, Ui_Pseudonym):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.regex = QRegExp("^[0-9]+$")
        self.validator = QRegExpValidator(self.regex)
        self.takeInput.setValidator(self.validator)

    def initUI(self):
        self.startButton.clicked.connect(self.start_game)
        self.takeButton.clicked.connect(self.take_stone)
        if self.stones.text() == "":
            self.number_stones = 0
        else:
            self.number_stones = int(self.stones.text())
        self.number_take_stones = 0
        self.flag = 1
        self.listWidget.clear()
        self.remainLcd.setText(str(self.number_stones))
        self.resultLabel.setText("")

    def start_game(self):
        if self.stones.text() == "":
            self.number_stones = 0
        else:
            self.number_stones = int(self.stones.text())
        self.number_take_stones = 0
        self.flag = 1
        self.listWidget.clear()
        self.remainLcd.setText(str(self.number_stones))
        self.resultLabel.setText("")
        if self.number_stones == 0:
            self.resultLabel.setText(f"{win}")

    def take_stone(self):
        if self.number_stones != 0 and self.takeInput.text() != "" and 0 < int(self.takeInput.text()) <= 3:
            try:
                flag = 1
                while flag != 0:
                    self.number_take_stones = int(self.takeInput.text())
                    self.number_stones -= self.number_take_stones
                    flag = 0
                    self.listWidget.addItem(f"{take} - {self.number_take_stones}")
                    if self.number_stones == 0:
                        self.resultLabel.setText(f"{win}")
                        self.remainLcd.setText(str(self.number_stones))
                        return ""
                if self.number_stones < 4:
                    self.number_take_stones = self.number_stones
                elif self.number_stones % 4 == 0:
                    self.number_take_stones = 1
                elif self.number_stones % 4 != 0 and self.number_stones > 3:
                    self.number_take_stones = self.number_stones % 4
                self.number_stones -= self.number_take_stones
                self.listWidget.addItem(f"{pctake} - {self.number_take_stones}")
                if self.number_stones == 0:
                    self.resultLabel.setText(f"{pcwin}")
                self.remainLcd.setText(str(self.number_stones))
            except Exception as ex:
                print(ex)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"{err}")
            msg.setInformativeText(f'{text}')
            msg.setWindowTitle("Error")
            msg.exec_()


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = Pseudonym()
    sx.show()
    sys.exit(sa.exec())
