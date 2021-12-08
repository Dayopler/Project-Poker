from gui.component.Component import Component
from PyQt5.QtWidgets import *


class ButtonComponent(Component):
    AVAILABLE_ACTION: tuple = ('follow', 'bet', 'add', 'giveup', 'nothing')

    def __init__(self, title: str, action: str):
        self.__title = title
        self.button = None

        # check if the action exist
        if action in self.AVAILABLE_ACTION:
            self.__action = action
        else:
            raise ValueError('action invalid')

    def __repr__(self):
        return f'represent button {self.__title}'

    def get(self, container, group):
        self.button = QPushButton(container)
        self.button.setObjectName(self.__title)
        self.button.setText(self.__title)
        self.button.clicked.connect(lambda: print(f'hello from {self.__action}'))
        group.addWidget(self.button)
