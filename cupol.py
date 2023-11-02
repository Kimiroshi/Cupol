import subprocess


class Cupol:
    def __init__(self):
        with open('current_settings.txt', 'r', encoding="utf-8") as f:
            self.settings = f.readlines()
            self.settings = [i.strip('\n') for i in self.settings]
        self.auto = False
        self.color = 'white'
        self.language = 'rus'
        self.log = self.settings[-2]
        self.psw = self.settings[-1]
        self.auto = self.settings[3]
        if self.settings[1] == 'Темная':
            self.color = 'black'
        else:
            self.color = 'white'

        if self.settings[2] == 'Русский':
            self.language = 'rus'
        else:
            self.language = 'eng'

    def start(self):
        # Это условие отрабатывает только в самый первый запуск приложения
        if self.settings[0] == 'True':
            q = open('current_settings.txt', 'w')
            q.close()
            with open('current_settings.txt', '+a', encoding="utf-8") as f:
                f.write("False" + '\n')
                f.write('Светлая' + '\n')
                f.write('Русский' + '\n')
                f.write('False' + '\n')
                f.write('zer' + '\n')
                f.write('zer')
            subprocess.Popen(['register.py'], shell=True, creationflags=subprocess.SW_HIDE)

        else:
            # Если включено "запомнить меня", то сразу открывать главную страницу
            if self.settings[3] == 'True':
                subprocess.Popen(['main.py'], shell=True, creationflags=subprocess.SW_HIDE)
            # В противном случае запускать страницу регистрации и ставить стандартные настройки
            else:
                subprocess.Popen(['register.py'], shell=True, creationflags=subprocess.SW_HIDE)
                q = open('current_settings.txt', 'w')
                q.close()
                with open('current_settings.txt', '+a', encoding="utf-8") as f:
                    f.write("False" + '\n')
                    f.write('Светлая' + '\n')
                    f.write('Русский' + '\n')
                    f.write('False' + '\n')
                    f.write('zer' + '\n')
                    f.write('zer')


starter = Cupol()

if __name__ == '__main__':
    starter.start()
