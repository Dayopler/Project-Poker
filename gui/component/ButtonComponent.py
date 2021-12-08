from gui.component.Component import Component
from PyQt5.QtWidgets import *


class ButtonComponent(Component):
    def __init__(self, title: str, action: str, button_horizontal_layout):
        self.__title = title
        self.__action = action
        self.container = button_horizontal_layout

    def __repr__(self):
        return 'represent button to do action on the game'

    def get(self):
        self.button_parole = QPushButton(self.container)
        self.button_parole.setObjectName(self.__title)
        self.button_parole.clicked.connect(lambda: print(f'hello from {self.__action}'))
