import unittest

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



class QueueTwoStacks(object):
    # Implement the enqueue and dequeue methods
    s1 = Stack()
    s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if(self.s1.size()==0) and (self.s2.size()==0):
            self.assertRaises(Exception)
        if (self.s2.size()==0):
            while (self.s1.size()>0):
                self.s2.push(self.s1.pop())
        return self.s2.pop()








# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)