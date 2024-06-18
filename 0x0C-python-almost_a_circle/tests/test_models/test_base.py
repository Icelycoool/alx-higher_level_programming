#!/usr/bin/python3
"""
Defines unittests for base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_automatic_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_base_specified_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string(self):
        obj = Base(89)
        json_str = Base.to_json_string([obj.to_dictionary()])
        self.assertEqual(json_str, '[{"id": 89}]')

    def test_from_json_string(self):
        json_str = '[{"id": 89}]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(obj_list[0].id, 89)

if __name__ == '__main__':
    unittest.main()