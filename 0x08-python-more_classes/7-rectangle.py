#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """
    Represents a rectangle.

    Attritubes:
        number_of_instances: Tracks the number of rectangles.
        print_symbol: Used to print the rectangle.
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
        __str__(self):
            Returns a string representation of the rectangle using `#`.
        __repr__(self):
            Returns a string representation that can recreate the instance.
        __del__(self):
            Destructor method called when an instance is about to be destroyed.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Returns a string representation of the rectangle using `#`.
        """
        rectangle_str = ""
        if self.width == 0 or self.height == 0:
            return rectangle_str

        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate
        a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

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

    def __del__(self):
        """
        Destructor method called when an instance is about to be destroyed.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
