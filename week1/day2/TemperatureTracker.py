import unittest


class TempTracker(object):
    # Implement methods to track the max, min, mean, and mode

    max = 0
    min = 110
    mean = 0
    mode = 0
    count = 0
    arr = []

    for i in range(111):
        arr.append(0)

    def insert(self, temperature):

        self.max = temperature if temperature > self.max else self.max
        self.min = temperature if temperature < self.min else self.min
        self.mean = ((self.mean * self.count) + temperature)/(self.count+1)
        self.count += 1
        self.arr[temperature] += 1
        temp = max(self.arr)
        temp_mode = [i for i, e in enumerate(self.arr) if e == temp]

        self.mode = temp_mode[0] if len(temp_mode) == 1 else temp_mode

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode



'''
tracker = TempTracker()

tracker.insert(50)
msg = 'failed on first temp recorded'
print(tracker.get_max())
print(tracker.get_min())
print(tracker.get_mean( ))
print(tracker.get_mode())

tracker.insert(80)
msg = 'failed on higher temp recorded'
print(tracker.get_max())
print(tracker.get_min())
print(tracker.get_mean())
print(tracker.get_mode())

tracker.insert(80)
msg = 'failed on third temp recorded'
print(tracker.get_max())
print(tracker.get_min())
print(tracker.get_mean())
print(tracker.get_mode())

tracker.insert(30)
msg = 'failed on lower temp recorded'
print(tracker.get_max())
print(tracker.get_min())
print(tracker.get_mean())
print(tracker.get_mode())

'''


# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)