#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """
    Class that defines property of a square.

    Attributes:
        size: size of a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Creates new instance of square.

        Args:
            __size (int): size of the square.
            __position (tuple): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Returns the position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter for position.

        Args: value (tuple): position of th esquare.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in rangegself.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
