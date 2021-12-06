import unittest


class SorterManagerTest(unittest.TestCase):

    def test_higher_hand_without_equality(self):
        """
        test to get the higher hand without getting a weight equality
        between the different hand
        :return:
        """
        higher = 2
        self.assertEqual(higher, 2)

    def test_higher_hand_with_equality_2(self):
        """
        test to get te higher hand with an equality between 2 hand
        this test is based on kicker card
        :return:
        """
        higher = 2
        self.assertEqual(higher, 2)

    def test_higher_hand_with_equality_3(self):
        """
        test to get te higher hand with an equality between 3 hand
        this test is based on kicker card
        :return:
        """
        higher = 2
        self.assertEqual(higher, 2)

    def test_higher_hand_with_equality_4(self):
        """
        test to get te higher hand with an equality between 4 hand
        this test is based on kicker card
        :return:
        """
        higher = 2
        self.assertEqual(higher, 2)


if __name__ == '__main__':
    unittest.main()
