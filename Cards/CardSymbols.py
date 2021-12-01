from enum import Enum, unique


@unique
class CardSymbols(Enum):
    HEART = 0
    CLUBS = 1
    DIAMONDS = 2
    SPADES = 3
