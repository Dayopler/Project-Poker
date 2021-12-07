import random

from PokerGame.DeckManager.Card import Card
from PokerGame.DeckManager.CardValues import CardValues
from PokerGame.DeckManager.CardColors import CardColors
from PokerGame.DeckManager.CardSymbols import CardSymbols


class Deck:

    # remove 4 to keep only enum values and remove built-in class methods provided
    minimum_size = (len(dir(CardValues))-4) * (len(dir(CardSymbols))-4)

    def __init__(self, deck_size: int = 52):
        """
        deck minimum_size represent the total of card the game will get inside
        :param deck_size:
        """
        # check if deck __size's correct
        if deck_size % self.minimum_size != 0:
            raise ValueError(f'deck must contain at least {self.minimum_size} cards')

        self.__size: int = deck_size

        # deck content
        self.__cards: list[Card] = self.__build()

    def __repr__(self):
        return f"represent deck contains {self.__size} card"

    def __iter__(self):
        return self.__cards

    def __next__(self) -> Card:
        self.__size -= 1
        return self.__cards.pop(0)

    def shuffle(self):
        """
        shuffle deck
        :return:
        """
        random.shuffle(self.__cards)

    def __build(self) -> list[Card]:
        """
        build new deck, which contain Cards object
        all the values are coming from enumerator class in Cards directory
        :return list:
        """
        cards_list: list[Card] = []

        # one card game __size is represented by minimum __size attribute
        # making this is to know how many card game we need in the deck
        total_card_game_in_deck = int(self.__size / self.minimum_size)

        total_symbol = len(dir(CardSymbols))-4
        total_value = len(dir(CardValues))-4

        for i in range(0, total_card_game_in_deck):
            for symbol in range(0, total_symbol):
                color = CardColors(symbol % 2)
                for value in range(0, total_value):
                    cards_list.append(Card(value=CardValues(value), symbol=CardSymbols(symbol), color=color))

        return cards_list

    @property
    def size(self) -> int:
        return self.__size
