from Cards.CardValues import CardValues
from Cards.CardColors import CardColors
from Cards.CardSymbols import CardSymbols


class Card:
    def __init__(self, value: CardValues, symbol: CardSymbols, color: CardColors):
        self.__value: CardValues = value
        self.__symbol: CardSymbols = symbol
        self.__color: CardColors = color

    def __repr__(self):
        return f'this card is the {self.__value.name} / {self.__symbol.name} / {self.__color.name}'

    @property
    def value(self):
        """
        get card value
        :return:
        """
        return self.__value.value

    @property
    def symbol(self):
        """
        get card symbol
        :return:
        """
        return self.__symbol.value

    @property
    def color(self):
        """
        get card color
        :return:
        """
        return self.__color.value

    @property
    def value_name(self):
        """
        get card string value
        :return:
        """
        return self.__value.name

    @property
    def symbol_name(self):
        """
        get card string symbol
        :return:
        """
        return self.__symbol.name

    @property
    def color_name(self):
        """
        get card string symbol
        :return:
        """
        return self.color.name
