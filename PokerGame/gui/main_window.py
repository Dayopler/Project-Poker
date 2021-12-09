from PyQt5.QtWidgets import QMainWindow
from PokerGame.gui.interface_content import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
