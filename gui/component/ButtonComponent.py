from gui.component.Component import Component
from gui.component.PlayerComponent import PlayerComponent
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

        if self.__action ==  'add' :
            self.button.clicked.connect(self.__addOnePiece)
        elif self.__action ==  'bet' :
            self.button.clicked.connect(self.__addOnePiece)
        elif self.__action ==  'giveup' :
            self.button.clicked.connect(self.__addOnePiece)
        elif self.__action ==  'nothing' :
            self.button.clicked.connect(self.__addOnePiece)
        elif self.__action ==  'follow' :
            self.button.clicked.connect(self.__addOnePiece)

        group.addWidget(self.button)


    def __addOnePiece(self, player: PlayerComponent):
        '''
        add One € to Player's bet
        :param player:
        :return:
        '''
        print(player.money)
        player.money = -1
        print(player.money)
