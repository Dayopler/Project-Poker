import unittest
from PokerGame.Players.Player import Player
from PokerGame.DeckManager.Card import *


class PlayerTest(unittest.TestCase):

    def test_player_name(self):
        name = 'john'
        player = Player(name=name)
        self.assertEqual(name, player.name)

    def test_player_money_default(self):
        player = Player(name='john')
        self.assertEqual(10, player.money)

    def test_player_money_custom(self):
        money = 100
        player = Player(name='john', money=money)
        self.assertEqual(money, player.money)

    def test_player_money_add(self):
        amount = 10
        money = 10
        total = amount+money

        player = Player(name='john', money=money)
        player.money = amount

        self.assertEqual(total, player.money)

    def test_player_money_reduce(self):
        amount = 10
        money = -10
        total = amount + money

        player = Player(name='john', money=money)
        player.money = amount

        self.assertEqual(total, player.money)

    def test_player_is_ia_false(self):
        player = Player(name='john')
        self.assertTrue(player.is_ia)

    def test_player_is_ia_true(self):
        player = Player(name='john', is_ia=True)
        self.assertTrue(player.is_ia)

    def test_player_card_default(self):
        player = Player(name='john')

        self.assertEqual([], player.cards)

    def test_player_add_card(self):
        card = Card(value=CardValues(0), symbol=CardSymbols(3), color=CardColors(1))

        player = Player(name='john')
        player.cards = card

        self.assertEqual([card], player.cards)

    def test_player_cant_add_more_than_2_cards(self):
        card = Card(value=CardValues(0), symbol=CardSymbols(3), color=CardColors(1))
        card2 = Card(value=CardValues(2), symbol=CardSymbols(3), color=CardColors(1))
        card3 = Card(value=CardValues(3), symbol=CardSymbols(3), color=CardColors(1))

        player = Player(name='john')
        player.cards = card
        player.cards = card2
        player.cards = card3

        self.assertEqual([card, card2], player.cards)

    def test_player_reset_hand(self):
        card = Card(value=CardValues(0), symbol=CardSymbols(3), color=CardColors(1))

        player = Player(name='john')
        player.cards = card

        cards = player.get_and_reset_hand()

        self.assertEqual([], player.cards)

    def test_player_is_small_blind_false(self):
        player = Player(name='john')

        self.assertFalse(player.is_small_blind)

    def test_player_is_small_blind_true(self):
        player = Player(name='john')
        player.is_small_blind = True
        self.assertTrue(player.is_small_blind)

    def test_player_is_big_blind_false(self):
        player = Player(name='john')
        self.assertFalse(player.is_big_blind)

    def test_player_is_big_blind_true(self):
        player = Player(name='john')
        player.is_big_blind = True
        self.assertTrue(player.is_big_blind)


if __name__ == '__main__':
    unittest.main()
