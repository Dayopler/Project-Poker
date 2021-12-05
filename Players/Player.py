from Cards.Card import Card


class Player:
    def __init__(self, name: str, money: int = 100, is_ia: bool = True):
        self.__name: str = name
        self.__money: int = money
        self.__is_ia: bool = is_ia
        self.__hand: list[Card] = []

    def __repr__(self):
        return f'represent the player {self.__name} is IA ? {self.__is_ia}'

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