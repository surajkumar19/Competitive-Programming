import unittest

temp_None = {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}


def find_rectangular_overlap(rect1, rect2):
    if rect1['left_x'] <= rect2['left_x']:
        (r1, r2) = (rect1, rect2)
    else:
        (r1, r2) = (rect2, rect1)

    if r1['left_x'] + r1['width'] <= r2['left_x']:
        return temp_None  # no r1 & r2 overlap

    left_x = max(r1['left_x'], r2['left_x'])
    right_x = min(r1['left_x'] + r1['width'], r2['left_x'] + r2['width'])
    width = right_x - left_x

    if rect1['bottom_y'] <= rect2['bottom_y']:
        (r1, r2) = (rect1, rect2)
    else:
        (r1, r2) = (rect2, rect1)

    if r1['bottom_y'] + r1['height'] <= r2['bottom_y']:
        return temp_None  #r2 is above r1

    lower_y = max(r1['bottom_y'], r2['bottom_y'])
    upper_y = min(r1['bottom_y'] + r1['height'], r2['bottom_y'] + r2['height'])
    height = upper_y - lower_y

    intersection = {
        'left_x': left_x,
        'bottom_y': lower_y,
        'width': width,
        'height': height
    }

    return intersection


# rect1 = {
#             'left_x': 1,
#             'bottom_y': 0,
#             'width': 3,
#             'height': 2,
#         }
# rect2 = {
#     'left_x': 3,
#     'bottom_y': 3,
#     'width': 3,
#     'height': 2,
# }
#
# print(find_rectangular_overlap(rect1, rect2))



# Tests

class Test(unittest.TestCase):
    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
