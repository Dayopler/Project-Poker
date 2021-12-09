import sys
from PokerGame.gui.main_window import Window
from PyQt5.QtWidgets import QApplication


def game():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())