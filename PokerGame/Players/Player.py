from PokerGame.DeckManager import Card


class Player:
    def __init__(self, name: str, money: int = 10, is_ia: bool = True, is_small_blind: bool = False, is_big_blind: bool = False):
        self.__name: str = name
        self.__money: int = money
        self.__is_ia: bool = is_ia
        self.__is_small_blind: bool = is_small_blind
        self.__is_big_blind: bool = is_big_blind
        self.__hand: list[Card] = []
        self.__isgiveup: bool = False

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
        """
        set the money amount

        :param amount:
        :return:
        """
        self.__money += amount

    @property
    def name(self) -> str:
        """
        get the player name
        :return str:
        """
        return self.__name

    @property
    def is_ia(self) -> bool:
        """
        know if the player is an IA or not
        :return bool:
        """
        return self.__is_ia

    @property
    def is_small_blind(self) -> bool:
        """
        know if the player is an IA or not
        :return bool:
        """
        return self.__is_small_blind

    @property
    def is_big_blind(self) -> bool:
        """
        know if the player is an IA or not
        :return bool:
        """
        return self.__is_big_blind

    @is_small_blind.setter
    def is_small_blind(self, is_small_blind: bool):
        """
        know if the player is small blind
        :return:
        """
        self.__is_small_blind = is_small_blind

    @is_big_blind.setter
    def is_big_blind(self, is_big_blind: bool):
        """
        know if the player is big blind
        :return:
        """
        self.__is_big_blind = is_big_blind

    @property
    def isgiveup(self) -> bool:
        """
        give up the round
        :return bool:
        """
        return self.__isgiveup

    @isgiveup.setter
    def isgiveup(self, isgiveup: bool):
        """
        give up the round
        :return bool:
        """
        self.__isgiveup = isgiveup
