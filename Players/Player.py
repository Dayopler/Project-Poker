from Cards.Card import Card


class Player:
    def __init__(self, name: str, money: int = 10, is_ia: bool = True):
        self.__name: str = name
        self.__money: int = money
        self.__is_ia: bool = is_ia
        self.__hand: list[Card] = []

    def __repr__(self):
        return f'represent the player {self.__name} has {self.__money}'

    def get_and_reset_hand(self) -> list[Card]:
        """
        return card from the player hand and set the list empty
        :return list[Card]:
        """
        cards = self.__hand
        self.__hand = []
        return cards

    @property
    def cards(self) -> list[Card]:
        """
        get card from the player hand
        :return list[Card]:
        """
        return self.__hand

    @cards.setter
    def cards(self, card: Card):
        """
        add a card in the player hand
        :param card:
        """
        if len(self.__hand) < 2:
            self.__hand.append(card)

    @property
    def money(self) -> int:
        """
        :return int:
        """
        return self.__money

    @money.setter
    def money(self, amount: int):
        self.__money += amount

    @property
    def name(self) -> str:
        """
        :return str:
        """
        return self.__name

    @property
    def is_ia(self) -> bool:
        """
        :return bool:
        """
        return self.__is_ia