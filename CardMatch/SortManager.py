from Sorter import Sorter
from Cards.Card import *


class SorterManager:

    def __init__(self, hands: list):
        self.__hands: list[Sorter] = [Sorter(hand=hand) for hand in hands]

    def __repr__(self):
        return 'compare hand and return the stronger'

    def get_higher(self) -> int:
        """
        TODO
            - check if the higher weight isn't present 2 times or more
            - if more than one unique higher weight compare on the higher card
            - return the hand with the higher card if needed

        return the index of the higher hand
        :return int:
        """
        return max(self.__compare())

    def __compare(self):
        """
        compare the given player's hand
        :return:
        """
        # stock the weight of compared hand
        hands_weight: list = []

        for hand in self.__hands:
            hands_weight.append(hand.sort())

        return hands_weight


if __name__ == '__main__':
    hand1 = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

    hand2 = [
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(3), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(7), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

    s = SorterManager(hands=[hand1, hand2])
    print(s.get_higher())