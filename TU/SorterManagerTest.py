import unittest
from PokerGame.CardMatch.SortManager import SorterManager
from PokerGame.DeckManager.Card import *


class SorterManagerTest(unittest.TestCase):

    def test_higher_hand_without_equality(self):
        """
        test to get the higher hand without getting a weight equality
        between the different hand
        :return:
        """
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

        higher_hand = SorterManager(players_hand=[hand1, hand2, hand3])

        self.assertEqual(0, higher_hand.get_higher())

    def test_higher_hand_with_equality_2(self):
        """
        test to get te higher hand with an equality between 2 hand
        this test is based on kicker card
        :return:
        """
        hand1 = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

        hand2 = [
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(5), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(7), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

        higher_hand = SorterManager(players_hand=[hand1, hand2])

        self.assertEqual(1, higher_hand.get_higher())

    def test_higher_hand_with_equality_3(self):
        """
        test to get te higher hand with an equality between 3 hand
        this test is based on kicker card
        :return:
        """
        hand1 = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
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
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

        higher_hand = SorterManager(players_hand=[hand1, hand2, hand3])

        self.assertEqual(2, higher_hand.get_higher())

    def test_higher_hand_with_equality_4(self):
        """
        test to get te higher hand with an equality between 4 hand
        this test is based on kicker card
        :return:
        """
        hand1 = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
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
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

        hand4 = [
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(3), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(2), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(0), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]

        higher_hand = SorterManager(players_hand=[hand1, hand2, hand3, hand4])

        self.assertEqual(2, higher_hand.get_higher())


if __name__ == '__main__':
    unittest.main()
