#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """
    Class that defines property of a square.

    Attributes:
        size: size of a square.
    """
    def __init__(self, size=0):
        """
        Creates new instance of square.

        Args:
            size: size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size.

        Args:
            value (int): size of a square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
