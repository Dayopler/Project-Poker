import unittest
from PokerGame.DeckManager.Deck import Deck


class DeckTest(unittest.TestCase):

    def test_total_card_default(self):
        deck = Deck()
        self.assertEqual(52, deck.size)

    def test_total_card_custom(self):
        deck = Deck(deck_size=104)
        self.assertEqual(104, deck.size)

    def test_total_card_after_card_remove(self):
        deck = Deck()
        deck.__next__()
        self.assertEqual(51, deck.size)


if __name__ == '__main__':
    unittest.main()
