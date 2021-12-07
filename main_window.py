import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from page import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.ui.action_Exit.triggered.connect(self.close)
        self.ui.action_Find_Replace.triggered.connect(
            self.findAndReplace
        )
        self.ui.action_About.triggered.connect(self.about)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
