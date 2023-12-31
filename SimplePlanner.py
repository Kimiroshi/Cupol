import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cupol import starter

if starter.color == 'black':
    from SimplePlanner_dark import Ui_MainWindow
else:
    from SimplePlanner_white import Ui_MainWindow


class SimplePlanner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        con = sqlite3.connect('tasks.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS plans(date TEXT, plan TEXT)""")
        res = cur.execute("""SELECT * FROM plans""").fetchall()
        for i in res:
            self.eventList.addItem(f'{i[0]} - {i[1]}')

    def initUI(self):
        self.events = []
        self.addEventBtn.clicked.connect(self.add_event)

    def add_event(self):
        if self.lineEdit.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка:")
            msg.setInformativeText('Вы не ввели задачу')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.events.append((self.calendarWidget.selectedDate(), self.timeEdit.time(),
                                self.lineEdit.text()))
            self.update_list()
            date = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
            time = self.timeEdit.time().toString('hh:mm:ss')
            task = self.lineEdit.text()
            con = sqlite3.connect('tasks.db')
            cur = con.cursor()
            cur.execute(f"""INSERT INTO plans(date, plan)
                         VALUES(?, ?)""", (f'{date} {time}', task))
            con.commit()

    def update_list(self):
        self.events = list(sorted(self.events))
        con = sqlite3.connect('tasks.db')
        cur = con.cursor()
        events = []
        for i in self.events:
            events.append(f"{i[0].toString('yyyy-MM-dd')} {i[1].toString('hh:mm:ss')} - {i[2]}")
        self.eventList.clear()
        self.eventList.addItems(events)


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = SimplePlanner()
    sx.show()
    sys.exit(sa.exec())
