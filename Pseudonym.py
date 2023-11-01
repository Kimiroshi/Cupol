import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import io


class Pseudonym(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Pseudonym.ui", self)
        self.initUI()

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
        self.remainLcd.display(str(self.number_stones))
        self.resultLabel.setText("")

    def start_game(self):
        if self.stones.text() == "":
            self.number_stones = 0
        else:
            self.number_stones = int(self.stones.text())
        self.number_take_stones = 0
        self.flag = 1
        self.listWidget.clear()
        self.remainLcd.display(str(self.number_stones))
        self.resultLabel.setText("")
        if self.number_stones == 0:
            self.resultLabel.setText("Победа пользователя!")

    def take_stone(self):
        if self.number_stones != 0 and self.takeInput.text() != "":
            flag = 1
            while flag != 0:
                self.number_take_stones = int(self.takeInput.text())
                if self.number_take_stones <= self.number_stones and 1 <= self.number_take_stones <= 3:
                    self.number_stones -= self.number_take_stones
                    flag = 0
                    self.listWidget.addItem(f"Игрок взял - {self.number_take_stones}")
                    if self.number_stones == 0:
                        self.resultLabel.setText("Победа пользователя!")
                        self.remainLcd.display(str(self.number_stones))
                        return ""
                else:
                    self.listWidget.addItem("Некорректный ход: " + str(self.number_take_stones))
            if self.number_stones < 4:
                self.number_take_stones = self.number_stones
            elif self.number_stones % 4 == 0:
                self.number_take_stones = 1
            elif self.number_stones % 4 != 0 and self.number_stones > 3:
                self.number_take_stones = self.number_stones % 4
            self.number_stones -= self.number_take_stones
            self.listWidget.addItem(f"Компьютер взял - {self.number_take_stones}")
            if self.number_stones == 0:
                self.resultLabel.setText("Победа компьютера!")
            self.remainLcd.display(str(self.number_stones))


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = Pseudonym()
    sx.show()
    sys.exit(sa.exec())
