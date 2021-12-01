from Cards.Card import Card


class Sorter:
    def __init__(self, hand: list[Card]):
        """
        - the hand represent the player/ai card he got

        - the kicker card represent in the ascending order the card with the highest
        value

        :param hand:
        """
        self.__cards_value: list[int] = [card.value for card in hand]
        self.__cards_symbol: list[int] = [card.symbol for card in hand]
        self.__cards_color: list[int] = [card.color for card in hand]

        self.__kicker_card = self.__cards_value
        self.__kicker_card.sort()

    def __repr__(self):
        return 'sort given hand for checking card match'

    def sort(self) -> int:
        """
        return an int which represent the weight of the hand
        there are represented here from the lowest to the highest
        :return int:
        """
        if self.__ispair():
            return 0
        elif self.__isdoublepair():
            return 1
        elif self.__isbrelan():
            return 2
        elif self.__isquinte():
            return 3
        elif self.__iscolor():
            return 4
        elif self.__isfull():
            return 5
        elif self.__issquare():
            return 6
        elif self.__isquinteflush():
            return 7
        elif self.__isquinteflushroyal():
            return 8

    def __ispair(self) -> bool:
        """
        :return bool:
        """
        repeat = {i: self.__cards_value.count(i) for i in self.__cards_value}
        values = list(repeat.values())
        return max(values) == 2 and values.count(max(values)) == 1

    def __isdoublepair(self) -> bool:
        """
        :return bool:
        """
        repeat = {i: self.__cards_value.count(i) for i in self.__cards_value}
        values = list(repeat.values())
        return max(values) == 2 and values.count(max(values)) == 2

    def __isbrelan(self) -> bool:
        """
        :return bool:
        """
        repeat = {i: self.__cards_value.count(i) for i in self.__cards_value}
        values = list(repeat.values())
        return max(values) == 3

    def __isquinte(self) -> bool:
        """
        :return bool:
        """
        self.__cards_value.sort()

        # check if its continuation
        for i in range(0, len(self.__cards_value) - 1):
            if self.__cards_value[i] + 1 != self.__cards_value[i + 1]:
                return False

        # check not the same color in the hand
        if self.__cards_color.count(0) == 5 or self.__cards_color.count(1) == 5:
            return False

        # check if contain at least 5 or 10 in the hand
        if 5 in self.__cards_value or 10 in self.__cards_value:
            return True

        return False

    def __iscolor(self) -> bool:
        """
        :return bool:
        """
        repeat = {i: self.__cards_symbol.count(i) for i in self.__cards_symbol}
        values = list(repeat.values())
        return max(values) == 5

    def __isfull(self) -> bool:
        """
        :return bool:
        """
        repeat = {i: self.__cards_value.count(i) for i in self.__cards_value}
        values = list(repeat.values())
        return len(values) == 2

    def __issquare(self) -> bool:
        """"
        :return bool:
        """
        repeat = {i: self.__cards_value.count(i) for i in self.__cards_value}
        values = list(repeat.values())
        return max(values) == 4

    def __isquinteflush(self) -> bool:
        """
        :return bool:
        """
        for i in range(0, len(self.__kicker_card) - 1):
            if self.__kicker_card[i] + 1 != self.__kicker_card[i + 1]:
                return False

        # check if index 0 is a clubs
        if self.__cards_symbol[0] != 1:
            return False

        # check if all symbol are clubs:
        if self.__cards_symbol.count(max(self.__cards_symbol)) == 5:
            return True

        return False

    def __isquinteflushroyal(self) -> bool:
        """
        1 for the last condition represent the diamonds in deck class
        :return bool:
        """
        # check the continuation
        if self.__kicker_card != [8, 9, 10, 11, 12]:
            return False

        if self.__cards_symbol.count(self.__cards_symbol[0]) != 5:
            return False

        if self.__cards_symbol[0] == 2:
            return True

        return False
