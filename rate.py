import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from rate_design import Ui_RateWindow


class RatePage(QMainWindow, Ui_RateWindow):
    def __init__(self):
        super().__init__()
        self.rating = 0
        self.setupUi(self)
        self.star1.clicked.connect(self.rate_sys)
        self.star2.clicked.connect(self.rate_sys)
        self.star3.clicked.connect(self.rate_sys)
        self.star4.clicked.connect(self.rate_sys)
        self.star5.clicked.connect(self.rate_sys)
        # Список всех звезд
        self.stars = [self.star1, self.star2, self.star3, self.star4, self.star5]

    def rate_sys(self):
        # Получение логина и имени текущего пользователя
        with open('current_settings.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            data = [i.strip('\n') for i in data]
            name = data[-1]
            login = data[-3]

        # Получение списка уже выбиравших рейтинг
        with open('rating.txt', 'r', encoding='utf-8') as f:
            users = f.readlines()
            users = [i.strip('\n').strip(': 1').strip(': 2').strip(': 3').strip(': 4').strip(': 5') for i in users]

        # Цикл снизу не учитывает саму выбранную звезду, поэтому еще + 1
        self.rating += 1

        # Пробегает от начала списка до выбранной звезды, прибавляя рейтинг
        for _ in self.stars[self.stars.index(self.star1):self.stars.index(self.sender())]:
            self.rating += 1

        # Записывает в файл, если этот аккаунт еще не выбирал рейтинг
        if f'{login}_{name}' not in users:
            with open('rating.txt', '+a', encoding='utf-8') as f:
                f.write(f'{login}_{name}: {self.rating} \n')
        else:
            # Получаем список всех оценок и заменяет оценку для текущего аккаунт
            with open('rating.txt', 'r', encoding='utf-8') as f:
                arr = f.readlines()
                arr = [i.strip('\n').strip(' ') for i in arr]
                arr[users.index(f'{login}_{name}')] = f'{login}_{name}: {self.rating}'

            # Очищаем файл рейтинга
            q = open('rating.txt', 'w')
            q.close()

            # Перезаписываем его с изменениями
            with open('rating.txt', 'w') as f:
                for i in arr:
                    f.write(i + '\n')
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RatePage()
    ex.show()
    sys.exit(app.exec_())
