import time

import pvporcupine
from pvrecorder import PvRecorder
from ear import listen
import speach
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow
from cupol_va_design import Ui_Cupol
import sys


keywords_paths = ['Cup-all_en_windows_v3_0_0.ppn']
porcupine = pvporcupine.create(access_key='Bj1AHInc4CAZFdDETzgPpr6SsoIW/1jMOE67vEhd6IIT0DhBYOZ3RQ==',
                               keyword_paths=keywords_paths)
recoder = PvRecorder(device_index=-1, frame_length=512)


class VoiceAssistent(QMainWindow, Ui_Cupol):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def cupol_va(self):
        try:
            recoder.start()
            while True:

                keyword_index = porcupine.process(recoder.read())
                if keyword_index >= 0:
                    speach.random_greet()
                    ans = listen()
                    if ans['text'] in ('включи калькулятор', 'запусти калькулятор', 'открой калькулятор'):
                        speach.random_ok()
                        subprocess.Popen(['Calculator.py'], shell=True, creationflags=subprocess.SW_HIDE)

                    elif ans['text'] in ('включи ним', 'запусти ним', 'открой ним'):
                        speach.random_ok()
                        subprocess.Popen(['NimStrikesBack.py'], shell=True, creationflags=subprocess.SW_HIDE)

                    elif ans['text'] in ('включи крестики-нолики', 'запусти крестики-нолики', 'открой крестики-нолики'):
                        speach.random_ok()
                        subprocess.Popen(['TicTacToe.py'], shell=True, creationflags=subprocess.SW_HIDE)

                    elif ans['text'] in ('включи анти плагиат', 'запусти анти плагиат', 'открой анти плагиат'):
                        speach.random_ok()
                        subprocess.Popen(['Antiplagiarism.py'], shell=True, creationflags=subprocess.SW_HIDE)

                    elif ans['text'] in ('включи записную книжку', 'запусти записную книжку', 'открой записную книжку'):
                        speach.random_ok()
                        subprocess.Popen(['MyNotes.py'], shell=True, creationflags=subprocess.SW_HIDE)

                    elif ans['text'] in ('включи псевдоним', 'запусти псевдоним', 'открой псевдоним'):
                        speach.random_ok()
                        subprocess.Popen(['Pseudonym.py'], shell=True, creationflags=subprocess.SW_HIDE)

                    elif ans['text'] in ('включи планировщик', 'запусти планировщик', 'открой планировщик'):
                        speach.random_ok()
                        subprocess.Popen(['SimplePlanner.py'], shell=True, creationflags=subprocess.SW_HIDE)
                    else:
                        speach.not_found()
                    print(ans)
        except KeyboardInterrupt:
            recoder.stop()
        finally:
            porcupine.delete()
            recoder.delete()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = VoiceAssistent()
    ex1 = VoiceAssistent()
    ex.show()
    ex1.cupol_va()
    sys.exit(app.exec_())
