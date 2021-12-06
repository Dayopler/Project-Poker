from Sorter import Sorter


class SorterManager:

    def __init__(self, hands: list):
        self.__hands: list[Sorter] = [Sorter(hand=hand) for hand in hands]

    def __repr__(self):
        return 'compare hand and return the stronger'

    def get_higher(self) -> int:
        """
        return the index of the higher hand
        :return int:
        """
        pass

    def compare(self):
        """
        compare the given player's hand
        :return:
        """
        # stock the weight of compared hand
        hands_weight: list = []

        for hand in self.__hands:
            hands_weight.append(hand.sort())

        print(hands_weight)


if __name__ == '__main__':
    s = SorterManager()
    s.compare()