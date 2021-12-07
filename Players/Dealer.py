from DeckManager.Deck import Deck


class Dealer:
    def __init__(self):
        self.__deck = Deck()
        self.__cash_prize = 0
        self.__deck.shuffle()

    def __repr__(self):
        return 'represent the dealer'

    def give_card(self):
        """
        return the next card contain in the deck
        :return:
        """
        return self.__deck.__next__()

    def reveal_cards(self, amount=3) -> list:
        """
        reveal given amount of card

        :param amount:
        :return list:
        """
        return [self.__deck.__next__() for i in range(0, amount)]

    @property
    def cash_prize(self) -> int:
        """
        return the cashprize
        :return int:
        """
        return self.__cash_prize

    @cash_prize.setter
    def cash_prize(self, amount):
        """
        add money in the cash prize
        :return:
        """
        self.__cash_prize += amount