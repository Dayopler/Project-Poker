from PokerGame.DeckManager.CardValues import CardValues
from PokerGame.DeckManager.CardColors import CardColors
from PokerGame.DeckManager.CardSymbols import CardSymbols


class Card:
    def __init__(self, value: CardValues, symbol: CardSymbols, color: CardColors):
        self.__value: CardValues = value
        self.__symbol: CardSymbols = symbol
        self.__color: CardColors = color

    def __repr__(self):
        return f'this card is the {self.__value.name} / {self.__symbol.name} / {self.__color.name}'

    @property
    def value(self) -> int:
        """
        get card value int format
        :return int:
        """
        return self.__value.value

    @property
    def symbol(self) -> int:
        """
        get card symbol int format
        :return int:
        """
        return self.__symbol.value

    @property
    def color(self) -> int:
        """
        get card color int format
        :return int:
        """
        return self.__color.value

    @property
    def value_name(self) -> str:
        """
        get card string value str format
        :return str:
        """
        return self.__value.name

    @property
    def symbol_name(self) -> str:
        """
        get card string symbol str format
        :return str:
        """
        return self.__symbol.name

    @property
    def color_name(self) -> str:
        """
        get card string symbol str format
        :return str:
        """
        return self.__color.name
