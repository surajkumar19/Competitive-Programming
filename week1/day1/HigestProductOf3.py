import unittest

def highest_product_of_3(A):
    # Calculate the highest product of three numbers
    assert (len(A) > 2), "Exception"

    A.sort()
    arr_size=len(A)
    maxvalue=A[0]*A[1]*A[2]

    for i in range(0, arr_size - 2):

        l = i + 1

        r = arr_size - 1
        while (l < r):

            if (A[i] * A[l] * A[r] > maxvalue):
                maxvalue=A[i] * A[l] * A[r]

            elif (A[i] * A[l] * A[r] < maxvalue):
                l += 1
            else:
                r -= 1

    return maxvalue

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
