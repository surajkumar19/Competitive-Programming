# O(n)
import unittest


class WordCloudData(object):
    def __init__(self, input_value_string):

        # Count the frequency of each word
        main_dict = {}

        input_value_string = input_value_string.lower()
        temp = ""
        for x in input_value_string:
            if ord('z') >= ord(x) >= ord('a') or x in ['-', '_', "'"]:
                temp += x
            else:
                if temp in ["", "_", "-", "'"]:
                    temp = ""
                    continue
                if temp in main_dict:
                    main_dict[temp] += 1
                else:
                    main_dict[temp] = 1
                temp = ""
        if temp not in ["", "_", "-", "'"]:
            if temp in main_dict:
                main_dict[temp] += 1
            else:
                main_dict[temp] = 1

        self.words_to_counts = main_dict


# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input_value = 'I like cake'

        word_cloud = WordCloudData(input_value)
        actual = word_cloud.words_to_counts

        expected = {'i': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input_value = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input_value)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input_value = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input_value)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'strawberry': 1, 'short': 1, 'yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input_value = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input_value)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input_value = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input_value)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input_value = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input_value)
        actual = word_cloud.words_to_counts

        expected = {"bakery": 1, "cakes": 1, "allie's": 1, "sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
