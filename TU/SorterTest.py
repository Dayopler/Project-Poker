import unittest

from CardMatch.Sorter import Sorter
from DeckManager.Card import Card


class MyTestCase(unittest.TestCase):
    """
    =========================================
    is pair test
    =========================================
    """
    def test_is_pair(self):
        hand = [
            Card(symbol=1, value=4),
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=2),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__ispair())

    def test_is_not_pair(self):
        hand = [
            Card(symbol=1, value=4),
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=5),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__ispair())

    """
    =========================================
    is double pair test
    =========================================
    """
    def test_is_double_pair(self):
        hand = [
            Card(symbol=1, value=3),
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=2),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isdoublepair())

    def test_is_not_double_pair(self):
        hand = [
            Card(symbol=1, value=2),
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=5),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isdoublepair())


    """
    =========================================
    is brelan test
    =========================================
    """
    def test_is_brelan(self):
        hand = [
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=2),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isbrelan())

    def test_is_not_brelan(self):
        hand = [
            Card(symbol=1, value=2),
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=5),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isbrelan())


    """
    =========================================
    is quinte test
    =========================================
    """
    def test_is_quinte(self):
        hand = [
            Card(symbol=1, value=1),
            Card(symbol=1, value=4),
            Card(symbol=1, value=3),
            Card(symbol=1, value=5),
            Card(symbol=1, value=2)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinte())

    def test_is_not_quinte(self):
        hand = [
            Card(symbol=1, value=11),
            Card(symbol=1, value=12),
            Card(symbol=1, value=13),
            Card(symbol=1, value=14),
            Card(symbol=1, value=15)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinte())

    """
    =========================================
    is square test
    =========================================
    """
    def test_is_square(self):
        hand = [
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__issquare())

    def test_is_not_square(self):
        hand = [
            Card(symbol=1, value=2),
            Card(symbol=1, value=2),
            Card(symbol=1, value=2),
            Card(symbol=1, value=5),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__issquare())

    """
    =========================================
    is full test
    =========================================
    """
    def test_is_full(self):
        hand = [
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=3),
            Card(symbol=1, value=1),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)
        self.assertTrue(sorter._Sorter__isfull())

    def test_is_not_full(self):
        hand = [
            Card(symbol=1, value=2),
            Card(symbol=1, value=2),
            Card(symbol=1, value=2),
            Card(symbol=1, value=5),
            Card(symbol=1, value=1)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isfull())

    """
    =========================================
    is quinte flush test
    =========================================
    """
    def test_is_quinte_flush(self):
        hand = [
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=4),
            Card(symbol=1, value=5),
            Card(symbol=1, value=6)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinteflush())

    def test_is_not_quinte_flush(self):
        hand = [
            Card(symbol=1, value=2),
            Card(symbol=1, value=3),
            Card(symbol=1, value=4),
            Card(symbol=2, value=5),
            Card(symbol=1, value=6)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflush())

    """
    =========================================
    is quinte flush royal test
    =========================================
    """
    def test_is_quinte_flush_royal(self):
        hand = [
            Card(symbol=1, value=8),
            Card(symbol=1, value=9),
            Card(symbol=1, value=10),
            Card(symbol=1, value=11),
            Card(symbol=1, value=12)
        ]
        sorter = Sorter(hand=hand)

        self.assertTrue(sorter._Sorter__isquinteflushroyal())

    def test_is_not_right_symbol_quinte_flush_royal(self):
        hand = [
            Card(symbol=1, value=8),
            Card(symbol=1, value=9),
            Card(symbol=2, value=10),
            Card(symbol=1, value=11),
            Card(symbol=1, value=12)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflushroyal())

    def test_is_not_right_value_quinte_flush_royal(self):
        hand = [
            Card(symbol=1, value=11),
            Card(symbol=1, value=7),
            Card(symbol=1, value=8),
            Card(symbol=1, value=9),
            Card(symbol=1, value=10)
        ]
        sorter = Sorter(hand=hand)
        self.assertFalse(sorter._Sorter__isquinteflushroyal())


if __name__ == '__main__':
    unittest.main()
