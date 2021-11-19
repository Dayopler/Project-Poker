import random


class Deck:
    cards_symbol: tuple = ('heart', 'diamonds', 'clubs', 'spades')
    cards_value: tuple = (
        'two', 'three', 'four', 'five', 'six', 'seven', 'height', 'nine', 'ten', 'jack', 'queen', 'king', 'as')

    minimum_size = len(cards_value) * len(cards_symbol)

    def __init__(self, deck_size: int = 52, seed: int = None):
        """
        deck minimum_size represent the total of card the game will get inside
        :param deck_size:
        """
        # check if deck minimum_size's correct
        if deck_size % self.minimum_size != 0:
            raise ValueError(f'deck must contain at least {self.minimum_size} cards')

        # size of the deck
        self.size: int = deck_size

        # deck content
        self.cards: list[tuple] = self.__build()

        # the deck seed
        self.__seed: int = None if seed is None else seed

    def __repr__(self):
        return "represent deck contains card"

    def shuffle(self):
        """
        shuffle deck
        :return:
        """
        self.__generate_seed()
        random.shuffle(self.cards)

    def __build(self) -> list[tuple]:
        """
        build new deck, it will return list of tuple
        tuple contain two value:
        - first index contain index of card value in cards_value
        - second index contain index of card symbol in cards_symbol
        :return list:
        """
        cards_list: list[tuple] = []

        for i in range(0, int(self.size / self.minimum_size)):
            for symbol in range(0, len(self.cards_symbol)):
                for value in range(0, len(self.cards_value)):
                    cards_list.append((value, symbol))

        return cards_list

    def __generate_seed(self):
        """
        get the seed for the deck
        :return:
        """
        if self.__seed is None:
            self.__seed = random.randint(1, 10000)

        random.seed(self.__seed)
        random.random()


if __name__ == '__main__':
    d = Deck()
    d.shuffle()
