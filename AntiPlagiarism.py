import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('AntiPlagiarism.ui', self)
        self.initUI()

    def initUI(self):
        self.checkBtn.clicked.connect(self.check)

    def check(self):
        text1 = list(set(self.text1.toPlainText().split("\n")))
        text2 = list(set(self.text2.toPlainText().split("\n")))
        identical_lines = 0
        various_lines = 0
        for i in text2:
            if i not in text1:
                various_lines += 1
            else:
                identical_lines += 1
        for i in text1:
            if i not in text2:
                various_lines += 1
        result = f"Тексты похожи на {(identical_lines / len(set(text1 + text2))) * 100:.2f}%, "
        if float(f"{(identical_lines / len(set(text1 + text2))) * 100:.2f}") < self.alert_value.value():
            result += "не плагиат"
        else:
            result += "плагиат"
        self.statusBar().showMessage(result)


if __name__ == '__main__':
    sa = QApplication(sys.argv)
    sx = AntiPlagiarism()
    sx.show()
    sys.exit(sa.exec())
