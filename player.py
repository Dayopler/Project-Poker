class Player:

    def __init__(self, name=None):
        self.__name = name
        self.__cards = []
        self.chips = 0


    def __str__(self):
        try:
            print("Le joueur {} a en sa possession les cartes {} et {}".format(self.__name, self.__cards[0],
                                                                               self.__cards[1]))
        except IndexError:
            print("Le joueur{} n'a pas de cartes".format(self.__name))

    def get_cards(self):
        return self.__cards

    def set_cards(self, card1, card2):
        self.__cards.append(card1)
        self.__cards.append(card2)

    def return_cards(self):
        cards_buffer = self.__cards
        self.__cards.clear()
        return cards_buffer


