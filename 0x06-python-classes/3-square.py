#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of a Square.

    Attributes:
        size: size of a square.
    """
    def __init__(self, size=0):
        """
        Creates new instance of square.

        Args:
            size: size of the square.
        """
        self__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns: the current square area.
        """
        return self.__size ** 2
