import unittest

from PokerGame.CardMatch.Sorter import Sorter
from PokerGame.DeckManager.Card import *


class SorterTest(unittest.TestCase):
    """
    =========================================
    is pair test.txt
    =========================================
    """
    def test_is_pair(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__ispair())

    def test_is_not_pair(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__ispair())

    """
    =========================================
    is double pair test.txt
    =========================================
    """
    def test_is_double_pair(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isdoublepair())

    def test_is_not_double_pair(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isdoublepair())


    """
    =========================================
    is brelan test.txt
    =========================================
    """
    def test_is_brelan(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isbrelan())

    def test_is_not_brelan(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isbrelan())


    """
    =========================================
    is quinte test.txt
    =========================================
    """
    def test_is_quinte(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinte())

    def test_is_not_quinte_continuation(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinte())

    def test_is_not_quinte_color(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertFalse(sorter._Sorter__isquinte())
    """
    =========================================
    is square test.txt
    =========================================
    """
    def test_is_square(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__issquare())

    def test_is_not_square(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__issquare())

    """
    =========================================
    is full test.txt
    =========================================
    """
    def test_is_full(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertTrue(sorter._Sorter__isfull())

    def test_is_not_full(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isfull())

    """
    =========================================
    is quinte flush test.txt
    =========================================
    """
    def test_is_quinte_flush(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinteflush())

    def test_is_not_quinte_flush_symbol(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflush())

    def test_is_not_quinte_flush_value(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(4), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(7), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflush())
    """
    =========================================
    is quinte flush royal test.txt
    =========================================
    """
    def test_is_quinte_flush_royal(self):
        hand = [
            Card(symbol=CardSymbols(2), value=CardValues(8), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(9), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(10), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(11), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(12), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinteflushroyal())

    def test_is_not_right_symbol_quinte_flush_royal(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(8), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(9), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(10), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(11), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(12), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflushroyal())

    def test_is_not_right_value_quinte_flush_royal(self):
        hand = [
            Card(symbol=CardSymbols(2), value=CardValues(7), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(9), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(10), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(11), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(12), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflushroyal())

    """
    =========================================
    is full test.txt
    =========================================
    """
    def test_is_color(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(3), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertTrue(sorter._Sorter__iscolor())

    def test_is_not_color(self):
        hand = [
            Card(symbol=CardSymbols(1), value=CardValues(2), color=CardColors(0)),
            Card(symbol=CardSymbols(2), value=CardValues(3), color=CardColors(1)),
            Card(symbol=CardSymbols(1), value=CardValues(1), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(5), color=CardColors(0)),
            Card(symbol=CardSymbols(1), value=CardValues(6), color=CardColors(0)),
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__iscolor())


if __name__ == '__main__':
    unittest.main()
