import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SimplePlanner.ui", self)
        self.initUI()

    def initUI(self):
        self.events = []
        self.addEventBtn.clicked.connect(self.add_event)

    def add_event(self):
        self.events.append((self.calendarWidget.selectedDate(), self.timeEdit.time(),
                            self.lineEdit.text()))
        self.update_list()

    def update_list(self):
        self.events = list(sorted(self.events))
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
