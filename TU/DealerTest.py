import unittest
from Players.Dealer import Dealer


class DealerTest(unittest.TestCase):

    def test_get_cash_prize(self):
        dealer = Dealer()

        self.assertEqual(0, dealer.cash_prize)

    def test_set_cash_prize(self):
        cash_prize = 10
        dealer = Dealer()
        dealer.cash_prize = 10

        self.assertEqual(cash_prize, dealer.cash_prize)

if __name__ == '__main__':
    unittest.main()
