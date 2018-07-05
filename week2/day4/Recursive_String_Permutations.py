# O(n * n!)
import unittest

def toString(List):
    return ''.join(List)

def get_permutations(string):

    # Generate all permutations of the input string
    list_val = []
    n = len(string)
    if n == 0:
        return {''}
    a = list(string)


    permute(a, 0, n - 1,list_val)

    return set(list_val)


def permute(a, l, r, lis):
    if l == r:
        lis.append(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, lis)
            a[l], a[i] = a[i], a[l]


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
