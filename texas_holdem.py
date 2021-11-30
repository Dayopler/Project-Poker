from player import *


class Game:
    def __init__(self):
        self.cards = []
        self.list_of_players = [Player]
        self.fold_players = []
        self.in_the_round_players = []
        self.cards_on_the_board = []
        self.highest_stake = 0
        self.pot = 0
        self.game_over = False
        self.winner = None

    def deal_players_cards(self):
        """TODO"""
        for players in self.list_of_players:
            players.set_cards()

    def deal_flop(self):
        """throws a card and deal the 3 first card on the board"""
        self.cards.pop()
        for i in range(3):
            self.cards_on_the_board.append(self.cards[0])
            self.cards.pop()

    def deal_river(self):
        """throws a card and deal the 4th card on the board"""
        self.cards.pop()
        self.cards_on_the_board.append(self.cards[0])
        self.cards.pop()

    def deal_turn(self):
        """FIXME : same method as deal_river"""
        """throws a card and deal the 5th and last card on the board"""
        self.cards.pop()
        self.cards_on_the_board.append(self.cards[0])
        self.cards.pop()

    def clear_board(self):
        """TODO"""
        """Reset the attributes, keeps the list_of_players, rebuild a deck and shuffles it, clear player cards,bets,
        chips.. """









    def add_player(self, player):
        self.list_of_players.append(player)


if __name__ == "__main__":
    Yohan = Player("Yohan")
