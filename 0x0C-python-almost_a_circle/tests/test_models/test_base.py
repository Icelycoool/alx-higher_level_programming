#!/usr/bin/python3
"""
Defines unittests for base.py
"""
import unittest
from models.base import Base


class TestSquare(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.s1 = Square(5, 10, 15, 1)
        self.s2 = Square(7, 20, 25, 2)

    def test_initialization(self):
        # Test initialization
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 10)
        self.assertEqual(self.s1.y, 15)
        self.assertEqual(self.s1.id, 1)

        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s2.x, 20)
        self.assertEqual(self.s2.y, 25)
        self.assertEqual(self.s2.id, 2)

    def test_size_property(self):
        # Test size property
        self.assertEqual(self.s1.size, 5)
        self.s1.size = 8
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.width, 8)
        self.assertEqual(self.s1.height, 8)

    def test_update_method(self):
        # Test update method
        self.s1.update(6, 30, 35, 3)
        self.assertEqual(self.s1.size, 6)
        self.assertEqual(self.s1.x, 30)
        self.assertEqual(self.s1.y, 35)
        self.assertEqual(self.s1.id, 3)

        self.s2.update(size=9, x=40, y=45, id=4)
        self.assertEqual(self.s2.size, 9)
        self.assertEqual(self.s2.x, 40)
        self.assertEqual(self.s2.y, 45)
        self.assertEqual(self.s2.id, 4)

    def test_to_dictionary_method(self):
        # Test to_dictionary method
        dict_s1 = self.s1.to_dictionary()
        self.assertEqual(dict_s1['size'], 5)
        self.assertEqual(dict_s1['x'], 10)
        self.assertEqual(dict_s1['y'], 15)
        self.assertEqual(dict_s1['id'], 1)

        dict_s2 = self.s2.to_dictionary()
        self.assertEqual(dict_s2['size'], 7)
        self.assertEqual(dict_s2['x'], 20)
        self.assertEqual(dict_s2['y'], 25)
        self.assertEqual(dict_s2['id'], 2)

    def test_string_representation(self):
        # Test string representation (__str__)
        self.assertEqual(str(self.s1), "[Square] (1) 10/15 - 5")
        self.assertEqual(str(self.s2), "[Square] (2) 20/25 - 7")

    def test_inheritance_from_rectangle(self):
        # Test inheritance from Rectangle
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)

        self.s1.width = 10
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)

    def test_inherited_methods_from_rectangle(self):
        # Test inherited methods from Rectangle
        self.s1.move(5, 5)
        self.assertEqual(self.s1.x, 15)
        self.assertEqual(self.s1.y, 20)
