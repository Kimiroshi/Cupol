import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from difflib import SequenceMatcher
from cupol import starter

if starter.color == "black":
    from AntiPlagiarism_dark import Ui_MainWindow
else:
    from AntiPlagiarism_white import Ui_MainWindow

if starter.language == "rus":
    text = 'Тексты похожи на'
    no = 'не плагиат'
    yes = 'плагиат'
else:
    text = 'The texts are similar to'
    no = 'not plagiarism'
    yes = 'plagiarism'


class AntiPlagiarism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBtn.clicked.connect(self.check)

    def check(self):
        text1 = ''.join(self.text1.toPlainText().split("\n")).replace(' ', '')
        text2 = ''.join(self.text2.toPlainText().split("\n")).replace(' ', '')
        result_n = SequenceMatcher(None, text1, text2).ratio()
        result = f"{text} {(result_n * 100):.2f}%, "
        if float(f"{(result_n * 100):.2f}") < self.alert_value.value():
            result += f"{no}"
        else:
            result += f"{yes}"
        self.statusBar().showMessage(result)


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = AntiPlagiarism()
    sx.show()
    sys.exit(sa.exec())