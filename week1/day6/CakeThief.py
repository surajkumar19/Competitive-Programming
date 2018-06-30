# O(mn)
import unittest
import math

def max_duffel_bag_value(cake_tuples, weight_capacity):
    maxValuesAtCapacities = [0]*(weight_capacity+1)


    for currentCapacity in range(weight_capacity+1):
        currentMaxValue = 0
        for cakeType in cake_tuples:

            if cakeType[0] == 0 and cakeType[1] != 0:
                return math.inf
            if (cakeType[0]<=currentCapacity):
                maxValueUsingCake = cakeType[1]+maxValuesAtCapacities[currentCapacity-cakeType[0]]
                currentMaxValue = max(maxValueUsingCake, currentMaxValue)

        maxValuesAtCapacities[currentCapacity] = currentMaxValue;

    # print(maxValuesAtCapacities)

    return maxValuesAtCapacities[weight_capacity]





# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        print(expected)
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
