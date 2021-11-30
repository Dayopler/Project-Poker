import random
from DeckManager.Card import Card


class Deck:
    minimum_size = len(Card.available_value) * len(Card.available_symbol)

    def __init__(self, deck_size: int = 52):
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
        self.__cards: list[Card] = self.__build()

    def __repr__(self):
        return f"represent deck contains {self.size} card"

    def __iter__(self):
        return self.__cards

    def __next__(self):
        self.size -= 1
        return self.__cards.pop(0)

    def shuffle(self):
        """
        shuffle deck
        :return:
        """
        random.shuffle(self.__cards)

    def __build(self) -> list[Card]:
        """
        build new deck, it will return list of tuple
        tuple contain two value:
        - first index contain index of card value in cards_value
        - second index contain index of card symbol in cards_symbol
        - third index contain index of card color
        :return list:
        """
        cards_list: list[Card] = []

        total_symbol = len(Card.available_symbol)
        total_value = len(Card.available_value)
        total_card_game_in_deck = int(self.size / self.minimum_size)

        for i in range(0, total_card_game_in_deck):
            for symbol in range(0, total_symbol):
                for value in range(0, total_value):
                    color = 0 if symbol % 2 == 0 else 1
                    cards_list.append(Card(value=value, symbol=symbol, color=color))

        return cards_list


if __name__ == '__main__':
    d = Deck()
    print(d.__next__())
    print(d.__next__())
