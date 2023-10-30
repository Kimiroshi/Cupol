import subprocess
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from cupol import Cupol
from settings_design import Ui_Settings
from threading import Timer
from datetime import datetime as dt

starter = Cupol()


class SettingsPage(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.account_button.clicked.connect(self.account_btn)
        self.rate_button.clicked.connect(self.rate_btn)
        self.home_button.clicked.connect(self.home_btn)
        self.save_button.clicked.connect(self.save_btn)

        # Правильное отображение текущей темы и языка
        self.theme_choose.setCurrentText('Темная' if starter.color == 'black' else 'Светлая')
        self.language_choose.setCurrentText('Русский' if starter.language == 'rus' else 'Английский')

        # Строки для автозапуска, он пока не работает
#        q = open('current_settings.txt', 'r')
#        self.autostart.setChecked(bool(q.readlines()[-1]))
#        q.close()

        self.time()

    # Открывает меню оценки
    def rate_btn(self):
        subprocess.Popen(['rate.py'], shell=True, creationflags=subprocess.SW_HIDE)

    # Открывает меню аккаунта
    def account_btn(self):
        subprocess.Popen(['account.py'], shell=True, creationflags=subprocess.SW_HIDE)
        exit()

    # Открывает главное меню
    def home_btn(self):
        subprocess.Popen(['main.py'], shell=True, creationflags=subprocess.SW_HIDE)
        exit()

    def save_btn(self):
        # Очистка файла текущих настроек от предыдущих
        q = open('current_settings.txt', 'w')
        q.close()

        # Запись новых данных и открытие домашней страницы
        with open('current_settings.txt', '+a', encoding="utf-8") as f:
            f.write("False" + '\n')
            f.write(self.theme_choose.currentText() + '\n')
            f.write(self.language_choose.currentText() + '\n')
            f.write(str(self.autostart.checkState()) + '\n')
            f.write(starter.log + '\n')
            f.write(starter.psw + '\n')
            f.write(starter.nam)
            subprocess.Popen(['main.py'], shell=True, creationflags=subprocess.SW_HIDE)

        # Получение всех текущих настроек
        with open('current_settings.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            data = [i.strip('\n') for i in data]

        # Запись их в cfg файл этого профиля
        q = open(f'cfgs/{starter.log}{starter.psw}{starter.nam}.txt', 'w')
        q.close()
        with open(f'cfgs/{starter.log}{starter.psw}{starter.nam}.txt', '+a', encoding='utf-8') as f:
            for i in data:
                f.write(i + '\n')

        # Строки для автостарта, он пока не работает
#        if bool(self.autostart.checkState()):
#            self.add_to_startup()
        exit()

    # Строки для автостарта, он пока не работает
#    def add_to_startup(self):
#        user = getpass.getuser()
#        path = 'C:\\Users\\%s\\PycharmProjects\\pythonProject1\\cupol.py' % user
#        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user
#        with open(bat_path + '\\' + 'open.bat', 'w+') as f:
#            f.write(r'start "cupol.py" %s' % path)

    # Функция для отображения времени
    def time(self):
        self.time_label.setText(dt.now().strftime("%H:%M"))
        Timer(1, self.time).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SettingsPage()
    ex.show()
    sys.exit(app.exec_())
