# O(n)
import unittest


def find_repeat(numbers_list):
    # Find the number that appears twice
    length = len(numbers_list)-1
    actual_value = length * (length + 1) // 2
    input_value = sum(numbers_list)

    return input_value - actual_value


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
