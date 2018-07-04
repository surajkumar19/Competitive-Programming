# O(n)
import unittest


def reverse(list_of_chars):
    # Reverse the input list of chars in place
    i = 0
    j = len(list_of_chars)

    if j == 0:
        return list_of_chars
    j -= 1
    while i < j:
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[j]
        list_of_chars[j] = temp

        i += 1
        j -= 1



    return list_of_chars


# Tests

class Test(unittest.TestCase):
    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)