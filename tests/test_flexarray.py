import unittest

from flexarray import FlexArray


class TestFlexArray(unittest.TestCase):
    def test_int_to_float(self):
        # define int FlexArray
        int_array = FlexArray([1, 2, 3, 4, 5])
        # check type is int
        self.assertEqual(int_array.type, 'B')
        # append float
        int_array.append(1.5)
        # chekc type is float
        self.assertEqual(int_array.type, 'f')
