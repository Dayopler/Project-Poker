import unittest

from CardMatch.Sorter import Sorter
from Cards.Card import Card


class MyTestCase(unittest.TestCase):
    """
    =========================================
    is pair test.txt
    =========================================
    """
    def test_is_pair(self):
        hand = [
            Card(symbol=1, value=4, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__ispair())

    def test_is_not_pair(self):
        hand = [
            Card(symbol=1, value=4, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=1, color=0)
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
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isdoublepair())

    def test_is_not_double_pair(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=1, color=0)
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
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isbrelan())

    def test_is_not_brelan(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=1, color=0)
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
            Card(symbol=1, value=1, color=0),
            Card(symbol=1, value=4, color=1),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=2, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinte())

    def test_is_not_quinte_continuation(self):
        hand = [
            Card(symbol=1, value=1, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=4, color=0),
            Card(symbol=1, value=6, color=0)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinte())

    def test_is_not_quinte_color(self):
        hand = [
            Card(symbol=1, value=1, color=0),
            Card(symbol=1, value=4, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=2, color=0)
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
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__issquare())

    def test_is_not_square(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=1, color=0)
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
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=1, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)
        self.assertTrue(sorter._Sorter__isfull())

    def test_is_not_full(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=1, color=0)
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
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=4, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=6, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinteflush())

    def test_is_not_quinte_flush_symbol(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=4, color=0),
            Card(symbol=2, value=5, color=0),
            Card(symbol=1, value=6, color=0)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflush())

    def test_is_not_quinte_flush_value(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=4, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=7, color=0)
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
            Card(symbol=1, value=8, color=0),
            Card(symbol=1, value=9, color=0),
            Card(symbol=1, value=10, color=0),
            Card(symbol=1, value=11, color=0),
            Card(symbol=1, value=12, color=0)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinteflushroyal())

    def test_is_not_right_symbol_quinte_flush_royal(self):
        hand = [
            Card(symbol=1, value=8, color=0),
            Card(symbol=1, value=9, color=0),
            Card(symbol=2, value=10, color=0),
            Card(symbol=1, value=11, color=0),
            Card(symbol=1, value=12, color=0)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflushroyal())

    def test_is_not_right_value_quinte_flush_royal(self):
        hand = [
            Card(symbol=1, value=11, color=0),
            Card(symbol=1, value=7, color=0),
            Card(symbol=1, value=8, color=0),
            Card(symbol=1, value=9, color=0),
            Card(symbol=1, value=10, color=0)
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
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=3, color=0),
            Card(symbol=1, value=1, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)
        self.assertTrue(sorter._Sorter__iscolor())

    def test_is_not_color(self):
        hand = [
            Card(symbol=1, value=2, color=0),
            Card(symbol=2, value=2, color=0),
            Card(symbol=1, value=2, color=0),
            Card(symbol=1, value=5, color=0),
            Card(symbol=1, value=1, color=0)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__iscolor())


if __name__ == '__main__':
    unittest.main()
