#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Attritubes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        width(self):
            Property getter for the rectangle's width.
        width(self, value):
            Property setter for the rectangle's width.
        height(self):
            Property getter for the rectangle's height.
        height(self, value):
            Property setter for the rangles's height.
        area(self):
            Calculates the area of the rectangle.
        perimeter(self):
            Calculates the perimeter of the rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueEror: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueEror: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
