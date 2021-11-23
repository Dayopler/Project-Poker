class Card:

    def __init__(self, symbol, value):
        self.__value: int = value
        self.__symbol: int = symbol

    def __repr__(self):
        return f'represent card {self.__symbol} / {self.__value}'

    def get_value(self):
        """
        get card value
        :return:
        """
        return self.__value

    def get_symbol(self):
        """
        get card value
        :return:
        """
        return self.__symbol

    value = property(fget=get_value)
    symbol = property(fget=get_symbol)
