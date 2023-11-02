import subprocess
import sys
from threading import Timer

from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime as dt
from cupol import starter
if starter.color == 'black':
    from dark_main_design import Ui_MainWindow
else:
    from main_design import Ui_MainWindow


class MainPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Создание перемены для работы со страницами (текущая стр, список стр, и словарь кнопок на каждой стр)
        self.current_page = 1
        self.pages_list = ["1"]
        self.pages = {"1": [self.app_1, self.app_2, self.app_3, self.app_4, self.app_5, self.app_6, self.app_7]}
        for i in self.pages_list:
            for j in self.pages[i]:
                j.clicked.connect(self.opener)

        # Словарь всех приложений и их кнопок, чтоб было удобно открывать
        self.apps = {
            self.app_1: "AntiPlagiarism.py",
            self.app_2: "Calculator.py",
            self.app_3: "MyNotes.py",
            self.app_4: "NimStrikesBack.py",
            self.app_5: "Pseudonym.py",
            self.app_6: "SimplePlanner.py",
            self.app_7: "TicTacToe.py",
        }

        self.account_button.clicked.connect(self.account_btn)
        self.settings_button.clicked.connect(self.settings_btn)

        self.time()

    # Функция для отображения предыдущей страницы
    # def previous_page(self):
    #     # Это условие проверяет, не выходим ли мы за гразинцы страниц и в случае успеха,
    #     # переводит текущую страницу на иную
    #     if self.current_page > 1:
    #         self.current_page -= 1
    #         # Пробегаемся по всем кнопкам, выключаем те, что не соответсвуют нынешней страннице
    #         for k in self.pages_list:
    #             if k != str(self.current_page):
    #                 for i in self.pages[k]:
    #                     i.setVisible(False)
    #                     i.setEnabled(False)
    #             if k == str(self.current_page):
    #                 for i in self.pages[k]:
    #                     i.setVisible(True)
    #                     i.setEnabled(True)
    #         self.cur_page.setText(str(self.current_page))

    # Функция для отображения следующей страницы
    # def next_page(self):
    #     # Это условие проверяет, не выходим ли мы за гразинцы страниц и в случае успеха,
    #     # переводит текущую страницу на иную
    #     if self.current_page < 2:
    #         self.current_page += 1
    #         # Пробегаемся по всем кнопкам, выключаем те, что не соответсвуют нынешней страннице
    #         for k in self.pages_list:
    #             if k != str(self.current_page):
    #                 for i in self.pages[k]:
    #                     i.setVisible(False)
    #                     i.setEnabled(False)
    #             if k == str(self.current_page):
    #                 for i in self.pages[k]:
    #                     i.setVisible(True)
    #                     i.setEnabled(True)
    #         self.cur_page.setText(str(self.current_page))

    # Открывает аккаунт
    def account_btn(self):
        subprocess.Popen(['account.py'], shell=True, creationflags=subprocess.SW_HIDE)
        self.t.cancel()
        exit()

    # Открывает настройки
    def settings_btn(self):
        subprocess.Popen(['settings.py'], shell=True, creationflags=subprocess.SW_HIDE)
        self.t.cancel()
        exit()

    # Открывает приложения
    def opener(self):
        app = self.apps[self.sender()]
        subprocess.Popen([app], shell=True, creationflags=subprocess.SW_HIDE)

    # Функция для отображения времени
    def time(self):
        self.time_label.setText(dt.now().strftime("%H:%M"))
        self.t = Timer(1, self.time)
        self.t.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    ex.show()
    sys.exit(app.exec_())
