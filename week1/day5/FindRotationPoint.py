# O(log n)
import unittest


def find_rotation_point(words):
    # Find the rotation point in the list
    low = 0;
    high = len(words) - 1
    while (low + 1 < high):
        mid = low + (high - low) // 2
        if(words[low] < words[high]):
            return low
        if (words[mid] < words[high]):
            high = mid
        if (words[mid] > words[low]):
            low = mid

    if words[low] < words[high]:
        return low
    else:
        return high


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)