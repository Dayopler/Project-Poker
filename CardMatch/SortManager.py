from Sorter import Sorter
from Cards.Card import *


class SorterManager:

    def __init__(self, players_hand: list):
        self.__hands: list[Sorter] = [Sorter(hand=hand) for hand in players_hand]

    def __repr__(self):
        return 'compare hand and return the stronger'

    def get_higher(self) -> int:
        """
        this method check which player get the higher hand,
        it'll return the player index to know directly
        who got the higher hand
        :return int:
        """
        hands_weight: list[int] = self.__get_hands_weight()
        max_weight = max(hands_weight)

        # check if there is equal max weight value
        if hands_weight.count(max_weight) > 1:
            equals_hand = [self.__hands[i].kicker_card for i in range(0, len(hands_weight)) if hands_weight[i] == max_weight]

            # get the player with the higher card in his hand
            for i in range(4, -1, -1):
                # get all cards value for given index
                cards_value = [hand[i] for hand in equals_hand]
                max_card_value = max(cards_value)

                # check if the max value is present only one time
                if cards_value.count(max_card_value) == 1:
                    # check which hand got this list to return player index
                    for hand in self.__hands:
                        if hand.kicker_card == equals_hand[cards_value.index(max_card_value)]:
                            return self.__hands.index(hand)

        else:
            return hands_weight.index(max_weight)



    def __get_hands_weight(self) -> list[int]:
        """
        compare the given player's hand
        :return list[int]:
        """
        # stock the weight of compared hand
        hands_weight: list = []

        for hand in self.__hands:
            hands_weight.append(hand.sort())

        return hands_weight


if __name__ == '__main__':
    hand1 = [
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

    hand2 = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(5), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(7), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

    hand3 = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(8), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

    s = SorterManager(players_hand=[hand1, hand2, hand3])
    print(s.get_higher())