from Cards.CardValues import CardValues
from Cards.CardColors import CardColors
from Cards.CardSymbols import CardSymbols


class Card:
    def __init__(self, value: CardValues, symbol: CardSymbols, color: CardColors):
        self.__value: CardValues = value
        self.__symbol: CardSymbols = symbol
        self.__color: CardColors = color

    def __repr__(self):
        return f'this card is the {self.__value.name} / {self.__symbol.name} / {self.color.name}'

    def get_value(self):
        """
        get card value
        :return:
        """
        return self.__value.value

    def get_symbol(self):
        """
        get card symbol
        :return:
        """
        return self.__symbol.value

    def get_color(self):
        """
        get card color
        :return:
        """
        return self.__color.value

    def get_value_name(self):
        """
        get card string value
        :return:
        """
        return self.__value.name

    def get_symbol_name(self):
        """
        get card string symbol
        :return:
        """
        return self.__symbol.name

    def get_color_name(self):
        """
        get card string symbol
        :return:
        """
        return self.color.name

    value = property(fget=get_value)
    symbol = property(fget=get_symbol)
    color = property(fget=get_color)

    value_name = property(fget=get_value_name)
    symbol_name = property(fget=get_symbol_name)
    color_name = property(fget=get_color_name)
