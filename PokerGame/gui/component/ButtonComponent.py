from PokerGame.gui.component.Component import Component
from PokerGame.gui.component.PlayerComponent import PlayerComponent
from PokerGame.Players.Dealer import Dealer
from PyQt5.QtWidgets import *


class ButtonComponent(Component):
    AVAILABLE_ACTION: tuple = ('follow', 'bet', 'add', 'giveup', 'nothing')

    def __init__(self, title: str, action: str, players: list[PlayerComponent], dealer: Dealer):
        self.__title = title
        self.__players = players
        self.__dealer = dealer
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

        if self.__action == 'add':
            self.button.clicked.connect(self.__addOnePiece)
        elif self.__action == 'bet':
            self.button.clicked.connect(self.__addOnePiece)
        elif self.__action == 'giveup':
            self.button.clicked.connect(self.__goToSleep)
        elif self.__action == 'nothing':
            self.button.clicked.connect(self.__keepWhatching)

        group.addWidget(self.button)

    def __addOnePiece(self):
        """
        add One € to Player's bet
        :param player:
        :return:
        """
        for player in self.__players:
            player.money = -1
            self.__dealer.cash_prize = 1
            player.set_money()

    def __keepWhatching(self):
        """
        pass your turn without do something and unveil mid card
        :return:
        """
        pass

    def __goToSleep(self):
        """
        leave this round because you have very bad cards
        :return:
        """
        for player in self.__players:
            if not player.is_ia:
                if not player.isgiveup:
                    player.isgiveup = True
                break
