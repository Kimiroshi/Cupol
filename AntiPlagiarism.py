import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from difflib import SequenceMatcher


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('AntiPlagiarism.ui', self)
        self.initUI()

    def initUI(self):
        self.checkBtn.clicked.connect(self.check)

    def check(self):
        text1 = ''.join(self.text1.toPlainText().split("\n")).replace(' ', '')
        text2 = ''.join(self.text2.toPlainText().split("\n")).replace(' ', '')
        result_n = SequenceMatcher(None, text1, text2).ratio()
        result = f"Тексты похожи на {(result_n * 100):.2f}%, "
        if float(f"{(result_n * 100):.2f}") < self.alert_value.value():
            result += "не плагиат"
        else:
            result += "плагиат"
        self.statusBar().showMessage(result)


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = AntiPlagiarism()
    sx.show()
    sys.exit(sa.exec())
