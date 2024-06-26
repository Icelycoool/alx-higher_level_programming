#!/usr/bin/python3
"""Module square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square"""
        return super().area()
