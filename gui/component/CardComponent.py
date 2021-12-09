from PokerGame.DeckManager.Card import *
from gui.component.Component import Component
from PyQt5.QtWidgets import *


class CardComponent(Card, Component):
    def __init__(self, value: CardValues, symbol: CardSymbols, color: CardColors, is_revealed: bool = False):
        super().__init__(value, symbol, color)
        self.is_revealed: bool = is_revealed

    def __repr__(self):
        return 'represent graphical card component'

    def get(self, MainWindow, horizontalLayoutWidget):
        self.player_card_infos = QVBoxLayout()
        self.player_card_infos.setObjectName(u"player_card_infos")

        self.label = QLabel(horizontalLayoutWidget)
        self.label.setObjectName(u"card_value")
        self.label.setText(f'card value: {self.value_name}')

        self.player_card_infos.addWidget(self.label)

        self.label_2 = QLabel(horizontalLayoutWidget)
        self.label_2.setObjectName(u"card_symbol")
        self.label.setText(f'card symbol {self.symbol_name}')

        self.player_card_infos.addWidget(self.label_2)

        self.label_3 = QLabel(horizontalLayoutWidget)
        self.label_3.setObjectName(u"card_color")
        self.label.setText(f'card color: {self.color_name}')

        self.player_card_infos.addWidget(self.label_3)
