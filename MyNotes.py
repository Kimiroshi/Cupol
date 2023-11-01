import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("MyNotes.ui", self)
        self.initUI()

    def initUI(self):
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        self.contactList.addItem(f"{self.contactName.text()} {self.contactNumber.text()}")


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = MyNotes()
    sx.show()
    sys.exit(sa.exec())
