from PokerGame.DeckManager.Card import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class CardComponent(Card):
    def __init__(self, value: CardValues = None, symbol: CardSymbols = None, color: CardColors = None, is_revealed: bool = False):
        super().__init__(value, symbol, color)
        self.is_revealed: bool = is_revealed

    def __repr__(self):
        return 'represent graphical card component'

