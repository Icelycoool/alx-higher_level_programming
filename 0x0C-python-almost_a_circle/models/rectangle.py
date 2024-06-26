#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle instance.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            x (int): The x coordinate of the new rectangle.
            y (int): The y coordinate of the new rectangle.
            id (int): The identity of the new rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the rectangel"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the new rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate for the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate for teh rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int : The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the rectangle using the `#` character.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the rectangle's attributes with the provided arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: A double pointer to a key/value for attributes to update.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args[:len(attrs)]):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
