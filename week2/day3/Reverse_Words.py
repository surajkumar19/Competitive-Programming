# O(n)
import unittest


def reverse_words(message):

    length_of_msg = len(message)
    if length_of_msg == 0:
        return message

    reverse(message, 0, length_of_msg)

    temp = 0
    for k in range(length_of_msg):
        if message[k] == " ":
            reverse(message, temp, k)
            temp = k + 1
    reverse(message, temp, length_of_msg)

    return message


def reverse(list_of_chars, initial, ending):
    # Reverse the input list of chars in place
    i = initial
    j = ending

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
    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
