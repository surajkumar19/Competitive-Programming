# O(n) time
import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    # Check if the shuffled deck is a single riffle of the halves
    pointer_1 = 0
    pointer_2 = 0
    pointer_3 = 0

    if len(half1) + len(half2) != len(shuffled_deck):
        return False

    while pointer_1 < len(half1) and pointer_2 < len(half2):
        if shuffled_deck[pointer_3] == half1[pointer_1]:
            pointer_1 += 1
        elif shuffled_deck[pointer_3] == half2[pointer_2]:
            pointer_2 += 1
        else:
            return False
        pointer_3 += 1

    while pointer_1 < len(half1):
        if shuffled_deck[pointer_3] == half1[pointer_1]:
            pointer_1 += 1
            pointer_3 += 1
        else:
            return False

    while pointer_2 < len(half2):
        if shuffled_deck[pointer_3] == half2[pointer_2]:
            pointer_2 += 1
            pointer_3 += 1
        else:
            return False

    return True


# Tests

class Test(unittest.TestCase):
    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
