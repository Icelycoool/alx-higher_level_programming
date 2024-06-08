#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 5, -4, -5, -6]), 5)

    def test_single_number(self):
        self.assertEqual(max_integer([9]), 9)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_same_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    if __name__ == '__main__':
        unittest.main()
