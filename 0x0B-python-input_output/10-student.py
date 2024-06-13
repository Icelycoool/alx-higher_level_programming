#!/usr/bin/python3
"""
Module that defines a student class
"""


class Student():
    """
    Student class

    Methods:
        __init__(self, first_name, last_name, age):
            Inializes the student class.
        to_json(self):
            Retrieves a dictionary representation of a student.
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
