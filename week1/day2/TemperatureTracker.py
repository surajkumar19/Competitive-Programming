import unittest


class TempTracker(object):
    # Implement methods to track the max, min, mean, and mode

    max = -1
    min = 111
    mean = 0
    max_freq = 0
    mode = 0
    count = 0
    temps = [0] * 111

    def insert(self, temperature):

        self.max = temperature if temperature > self.max else self.max
        self.min = temperature if temperature < self.min else self.min
        self.mean = ((self.mean * self.count) + temperature)/(self.count+1)
        self.count += 1
        self.temps[temperature] += 1
        if self.temps[temperature] > self.max_freq:
            self.max_freq = self.temps[temperature]
            self.mode = [temperature]
        elif self.temps[temperature] == self.max_freq:
            self.mode.append(temperature)

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        if len(self.mode) == 1:
            return self.mode[0]
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
