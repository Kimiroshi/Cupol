import sqlite3
import sys
import re
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from cupol import starter
if starter.color == "black":
    interface = "MyNotes_dark.ui"
else:
    interface = "MyNotes.ui"


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(interface, self)
        self.initUI()
        self.rgx_phone = re.compile("(?:\+?\(?\d{2,3}?\)?\D?)?\d{4}\D?\d{4}")
        con = sqlite3.connect('phones.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS numbers(name TEXT, phone TEXT)""")
        res = cur.execute("""SELECT * FROM numbers""").fetchall()
        for i in res:
            self.contactList.addItem(f'{i[0]} {i[1]}')
        con.close()

    def initUI(self):
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        phone = (self.contactNumber.text().replace(' ', '').replace('(', '').replace(')', '').replace('-', '').
                 replace('8', '+7'))
        con = sqlite3.connect('phones.db')
        cur = con.cursor()
        res = cur.execute(f"""SELECT * FROM numbers 
        WHERE phone = ?""", (self.contactNumber.text(), )).fetchall()
        if re.match(self.rgx_phone, phone) and not res and len(phone) == 12 and self.contactName.text() != '':
            self.contactList.addItem(f"{self.contactName.text()} {self.contactNumber.text()}")
            cur.execute(f"""INSERT INTO numbers(name, phone) 
                         VALUES(?, ?)""", (self.contactName.text(), self.contactNumber.text()))
        con.commit()


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = MyNotes()
    sx.show()
    sys.exit(sa.exec())
