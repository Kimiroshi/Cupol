import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('TicTacToe.ui', self)
        self.initUI()

    def initUI(self):
        self.step_number = 0
        self.active_symbol = "X"
        self.selected_symbol = "X"

        self.X_RadioButton.toggled.connect(self.toogle_symbol)
        self.O_RadioButton.toggled.connect(self.toogle_symbol)

        self.button_grid = [[], [], []]
        self.symbols = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.button_grid[0].append(self.btn_1)
        self.button_grid[0].append(self.btn_2)
        self.button_grid[0].append(self.btn_3)
        self.button_grid[1].append(self.btn_4)
        self.button_grid[1].append(self.btn_5)
        self.button_grid[1].append(self.btn_6)
        self.button_grid[2].append(self.btn_7)
        self.button_grid[2].append(self.btn_8)
        self.button_grid[2].append(self.btn_9)
        for i in range(3):
            for n in range(3):
                self.button_grid[i][n].clicked.connect(self.new_step)

        self.new_game_button.clicked.connect(self.new_game)
    def new_step(self):
        if self.sender().text() == "":
            if (self.selected_symbol == "X" and self.step_number == 0) or (self.selected_symbol == "X" and
                                                                           self.step_number % 2 == 0) or \
                    (self.selected_symbol == "O" and self.step_number % 2 == 1):
                self.sender().setText("X")
            else:
                self.sender().setText("O")
            self.step_number += 1
        for i in range(len(self.symbols)):
            for n in range(len(self.symbols[i])):
                self.symbols[i][n] = self.button_grid[i][n].text()
        if (len(set(self.symbols[0])) == 1 and self.symbols[0][0] != "") or \
                (len({self.symbols[0][0], self.symbols[1][0], self.symbols[2][0]}) == 1 and self.symbols[0][0] != ""):
            self.result_label.setText(f"Победил {self.symbols[0][0]}!")
            for i in range(len(self.button_grid)):
                for n in range(len(self.button_grid[i])):
                    self.button_grid[i][n].setEnabled(False)
        elif (len(set(self.symbols[1])) == 1 and self.symbols[1][1] != "") or \
                (len({self.symbols[0][1], self.symbols[1][1], self.symbols[2][1]}) == 1 and
                 self.symbols[1][1] != "") or \
                (len({self.symbols[0][0], self.symbols[1][1], self.symbols[2][2]}) == 1 and
                 self.symbols[1][1] != "") or \
                (len({self.symbols[0][2], self.symbols[1][1], self.symbols[2][0]}) == 1 and
                 self.symbols[1][1] != ""):
            self.result_label.setText(f"Победил {self.symbols[1][1]}!")
            for i in range(len(self.button_grid)):
                for n in range(len(self.button_grid[i])):
                    self.button_grid[i][n].setEnabled(False)
        elif (len(set(self.symbols[2])) == 1 and self.symbols[2][2] != "") or \
                (len({self.symbols[0][2], self.symbols[1][2], self.symbols[2][2]}) == 1 and self.symbols[2][2] != ""):
            self.result_label.setText(f"Победил {self.symbols[2][2]}!")
            for i in range(len(self.button_grid)):
                for n in range(len(self.button_grid[i])):
                    self.button_grid[i][n].setEnabled(False)
        elif "" not in self.symbols[0] + self.symbols[1] + self.symbols[2]:
            self.result_label.setText("Ничья!")
            for i in range(len(self.button_grid)):
                for n in range(len(self.button_grid[i])):
                    self.button_grid[i][n].setEnabled(False)

    def toogle_symbol(self, s):
        if s:
            self.selected_symbol = self.sender().text()
        self.new_game()
    def new_game(self):
        self.symbols = [["", "", ""], ["", "", ""], ["", "", ""]]
        for i in range(len(self.button_grid)):
            for n in range(len(self.button_grid[i])):
                self.button_grid[i][n].setText("")
                self.button_grid[i][n].setEnabled(True)
        self.active_symbol = self.selected_symbol
        self.step_number = 0
        self.result_label.setText("")


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = TicTacToe()
    sx.show()
    sys.exit(sa.exec())
