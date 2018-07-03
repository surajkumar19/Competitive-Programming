import unittest

dict = {'(': ')', '[': ']', '{': '}'}
dict_keys = dict.keys()

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def is_valid(code):
    # Determine if the input code is valid
    s1 = Stack()


    for x in code:
        if x in dict_keys:
            s1.push(x)
        else:
            if(s1.size()==0):
                return False
            temp = s1.pop()
            if ( dict[temp] != x):
                return False


    return s1.size()==0


# Tests

class Test(unittest.TestCase):
    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)