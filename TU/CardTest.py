import unittest
from Cards.Card import *


class CardTest(unittest.TestCase):

    def test_card_name_value(self):
        card = Card(value=CardValues(4), symbol=CardSymbols(2), color=CardColors(1))
        self.assertEqual('SIX', card.value_name)

    def test_card_name_symbol(self):
        card = Card(value=CardValues(4), symbol=CardSymbols(0), color=CardColors(1))
        self.assertEqual('HEART', card.symbol_name)

    def test_card_name_color(self):
        card = Card(value=CardValues(4), symbol=CardSymbols(0), color=CardColors(1))
        self.assertEqual('BLACK', card.color_name)

    def test_card_value(self):
        value: int = 1
        card = Card(value=CardValues(value), symbol=CardSymbols(2), color=CardColors(1))
        self.assertEqual(value, card.value)

    def test_card_symbol(self):
        symbol: int = 3
        card = Card(value=CardValues(4), symbol=CardSymbols(symbol), color=CardColors(1))
        self.assertEqual(symbol, card.symbol)

    def test_card_color(self):
        color: int = 1
        card = Card(value=CardValues(4), symbol=CardSymbols(0), color=CardColors(color))
        self.assertEqual(color, card.color)


if __name__ == '__main__':
    unittest.main()
