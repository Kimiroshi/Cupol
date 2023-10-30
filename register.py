import sys
import subprocess
import sqlite3
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from register_design import Ui_RegisterPage


class RegisterPage(QMainWindow, Ui_RegisterPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Создание валидаторов, отвечающих за ограничения на ввод логина, пароля, имени
        self.regex = QRegExp("^[A-Za-z0-9]+$")
        self.regex1 = QRegExp("^[A-Za-zА-Яа-я]+$")
        self.validator = QRegExpValidator(self.regex)
        self.validator1 = QRegExpValidator(self.regex1)
        self.login_line.setValidator(self.validator)
        self.password_line.setValidator(self.validator)
        self.name_line.setValidator(self.validator1)

        self.login_button.clicked.connect(self.login_btn)
        self.register_button.clicked.connect(self.reg_btn)

        # Инициализация иконок для кнопки показать/спрятать пароль
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cross_icon = QtGui.QIcon()
        self.cross_icon.addPixmap(QtGui.QPixmap("icons/eye-crossed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # Установка стандартного значения для поля пароля и кнопки
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.hide_password_button.clicked.connect(self.hide_btn)
        self.hide_password_button.setIcon(self.icon)
        self.hide_password_button.setIconSize(QtCore.QSize(35, 35))

        # Создание БД и таблицы в ней
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS data(login TEXT, password TEXT, name TEXT, cfg TEXT)""")
        con.close()

    # Кнопка логина
    def login_btn(self):
        res = self.check_data()
        login = self.login_line.text()
        password = self.password_line.text()
        name = self.name_line.text()
        # Проверка на ошибку
        if not res:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка:")
            msg.setInformativeText('Такого аккаунта не существует или вы не заполнили все поля')
            msg.setWindowTitle("Error")
            msg.exec_()
        # Запись настроек из cfg текущего аккаунт в текущие настройки приложения
        else:
            with open(f'cfgs/{login}{password}{name}.txt', 'r', encoding='utf-8') as f:
                data = f.readlines()
                data = [i.strip('\n') for i in data]
            q = open('current_settings.txt', 'w')
            q.close()
            with open(f'current_settings.txt', '+a', encoding='utf-8') as f:
                for n, i in enumerate(data):
                    if n == 3:
                        f.write(str(self.remember_box.isChecked()) + '\n')
                    else:
                        f.write(i + '\n')
            #  Открытие домашней странницы
            self.go_home()

    # Проверяет есть ли введенные данные в БД
    def check_data(self):
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()
        login = self.login_line.text()
        password = self.password_line.text()
        name = self.name_line.text()
        res = cur.execute(f"""SELECT * FROM data 
        WHERE login = ? and password = ? and name = ? and cfg = ?""",
                          (login, password, name, f'cfgs/{login}{password}{name}.txt')).fetchall()
        con.commit()
        con.close()
        return res

    # Кнопка регистрации
    def reg_btn(self):
        res = self.check_data()
        login = self.login_line.text()
        password = self.password_line.text()
        name = self.name_line.text()
        cfgpath = f'cfgs/{login}{password}{name}.txt'
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()

        # Проверка на существование аккаунта с такими данными
        if res:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка:")
            msg.setInformativeText('Похоже такой аккаунт уже существует')
            msg.setWindowTitle("Error")
            msg.exec_()

        # Запись в БД данных о новом аккаунте, сохранение его cfg в специальной папке и открытие домашней страницы
        elif all((login != '', password != '', name != '')) and not res:
            cur.execute(f"""INSERT INTO data(login, password, name, cfg) 
             VALUES(?, ?, ?, ?)""", (login, password, name, cfgpath))
            con.commit()
            self.set_cfg()
            os.rename(f'{login}{password}{name}.txt', cfgpath)
            self.go_home()

        # Проверка на пустые поля
        else:
            login = self.login_line.text()
            password = self.password_line.text()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка:")
            if login == '':
                msg.setInformativeText('Вы не ввели логин!')
            elif password == '':
                msg.setInformativeText('Вы не ввели пароль!')
            else:
                msg.setInformativeText('Вы не ввели имя!')
            msg.setWindowTitle("Error")
            msg.exec_()
        con.close()

    # Записывает стандартные настройки (но указывает логин, пароль, имя, статус кнопки "запомнить меня") в cfg,
    # соответсвующий этому аккаунту и в текущие настройки.
    # часть настроек берется стандартной, потому что на этапе регистрации их никак не поменять,
    # они будут всегда одинаковы в этот момент
    def set_cfg(self):
        login = self.login_line.text()
        password = self.password_line.text()
        name = self.name_line.text()
        q = open(f'{login}{password}{name}.txt', 'w')
        q.close()
        with open(f'{login}{password}{name}.txt', '+a', encoding='utf-8') as f:
            f.write('False' + '\n')
            f.write('Светлая' + '\n')
            f.write('Русский' + '\n')
            f.write(str(self.remember_box.isChecked()) + '\n')
            f.write(login + '\n')
            f.write(password + '\n')
            f.write(name + '\n')
        q = open(f'current_settings.txt', 'w')
        q.close()
        with open('current_settings.txt', '+a', encoding='utf-8') as f:
            f.write('False' + '\n')
            f.write('Светлая' + '\n')
            f.write('Русский' + '\n')
            f.write(str(self.remember_box.isChecked()) + '\n')
            f.write(login + '\n')
            f.write(password + '\n')
            f.write(name + '\n')

    # Открыть домашнюю страницу
    def go_home(self):
        subprocess.Popen(['main.py'], shell=True, creationflags=subprocess.SW_HIDE)
        exit()

    def hide_btn(self):
        # Проверка на то, скрыт ли пароль
        if self.password_line.echoMode() == 2:
            # Показать пароль
            self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.hide_password_button.setIcon(self.cross_icon)
            self.hide_password_button.setIconSize(QtCore.QSize(35, 35))
        else:
            # Скрыть пароль
            self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
            self.hide_password_button.setIcon(self.icon)
            self.hide_password_button.setIconSize(QtCore.QSize(35, 35))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RegisterPage()
    ex.show()
    sys.exit(app.exec())
