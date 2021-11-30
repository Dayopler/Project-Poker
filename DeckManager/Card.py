class Card:
    available_symbol: tuple[tuple[str]] = ('heart', 'clubs', 'diamonds', 'spades')
    available_value: tuple[str] = ('two', 'three', 'four', 'five', 'six', 'seven', 'height', 'nine', 'ten', 'jack', 'queen', 'king', 'as')
    available_color: tuple[str] = ('red', 'black')

    def __init__(self, symbol: int, value: int, color: int):
        self.__value: int = value
        self.__symbol: int = symbol
        self.__color: int = color

        try:
            self.__string_value: str = self.available_value[value]
            self.__string_symbol: str = self.available_symbol[symbol]
            self.__string_color: str = self.available_color[color]
        except IndexError as e:
            raise IndexError(f'incorrect index to get the string value {e}')

    def __repr__(self):
        return f'this card is the {self.__string_value} / {self.__string_symbol} / {self.__string_color}'

    def get_value(self):
        """
        get card value
        :return:
        """
        return self.__value

    def get_symbol(self):
        """
        get card symbol
        :return:
        """
        return self.__symbol

    def get_color(self):
        """
        get card color
        :return:
        """
        return self.__color

    def get_string_value(self):
        """
        get card string value
        :return:
        """
        return self.__string_value

    def get_string_symbol(self):
        """
        get card string symbol
        :return:
        """
        return self.__string_symbol

    value = property(fget=get_value)
    symbol = property(fget=get_symbol)
    color = property(fget=get_color)

    value_string = property(fget=get_string_value)
    symbol_string = property(fget=get_string_symbol)
