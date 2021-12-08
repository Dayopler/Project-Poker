from PokerGame.DeckManager.Card import *
from gui.component.Component import Component
from PyQt5.QtWidgets import *


class CardComponent(Card, Component):
    def __init__(self, value: CardValues = None, symbol: CardSymbols = None, color: CardColors = None, is_revealed: bool = False):
        super().__init__(value, symbol, color)
        self.is_revealed: bool = is_revealed

    def __repr__(self):
        return 'represent graphical card component'

    def get(self, MainWindow, horizontalLayoutWidget):
        self.card = QFrame(horizontalLayoutWidget)
        self.card.setObjectName(u"card2")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.card.setFrameShadow(QFrame.Raised)