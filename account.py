import sys
import subprocess
from cupol import Cupol
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from account_design import Ui_AccountWindow
from threading import Timer
from datetime import datetime as dt

starter = Cupol()


class AccountPage(QMainWindow, Ui_AccountWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_line.setText(starter.log)
        self.password_line.setText(starter.psw)
        self.name_line.setText(starter.nam)
        self.hide_password_button.clicked.connect(self.hide_btn)
        self.home_button.clicked.connect(self.home_btn)

        # Установка стандартного режима для графы пароля
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        # Инициализация иконок для кнопки скрытия пароля
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cross_icon = QtGui.QIcon()
        self.cross_icon.addPixmap(QtGui.QPixmap("icons/eye-crossed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.leave_account_button.clicked.connect(self.leave_btn)

        self.settings_button.clicked.connect(self.settings_btn)
        self.time()

    # Функция для кнопки скрыть/показать пароль
    def hide_btn(self):
        # Проверка на то, скрыт ли пароль
        if self.password_line.echoMode() == 2:
            # Показать пароль и поменять иконку кнопки
            self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.hide_password_button.setIcon(self.cross_icon)
            self.hide_password_button.setIconSize(QtCore.QSize(35, 35))
        else:
            # Скрыть пароль и поменять иконку кнопки
            self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
            self.hide_password_button.setIcon(self.icon)
            self.hide_password_button.setIconSize(QtCore.QSize(35, 35))

    # Открывает домашнюю страницу
    def home_btn(self):
        subprocess.Popen(['main.py'], shell=True, creationflags=subprocess.SW_HIDE)
        exit()

    # Открывает настройки
    def settings_btn(self):
        subprocess.Popen(['settings.py'], shell=True, creationflags=subprocess.SW_HIDE)
        exit()

    # Отвечает за выход из аккаунта, октрывая меню регистрации
    def leave_btn(self):
        with open('current_settings.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            data = [i.strip('\n') for i in data]

        q = open(f'cfgs/{starter.log}{starter.psw}{starter.nam}.txt', 'w')
        q.close()
        with open(f'cfgs/{starter.log}{starter.psw}{starter.nam}.txt', '+a', encoding='utf-8') as f:
            for i in data:
                f.write(i + '\n')

        q = open(f'current_settings.txt', 'w')
        q.close()
        with open('current_settings.txt', '+a', encoding="utf-8") as f:
            f.write("False" + '\n')
            f.write('Светлая' + '\n')
            f.write('Русский' + '\n')
            f.write('False' + '\n')
            f.write('zer' + '\n')
            f.write('zer' + '\n')
            f.write('zer')
            subprocess.Popen(['register.py'], shell=True, creationflags=subprocess.SW_HIDE)
        exit()

    # Отвечает за отображение времени
    def time(self):
        self.time_label.setText(dt.now().strftime("%H:%M"))
        Timer(1, self.time).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AccountPage()
    ex.show()
    sys.exit(app.exec())