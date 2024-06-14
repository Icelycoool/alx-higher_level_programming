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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """Get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle"""
            self.__width = value

        @property
        def height(self):
            """Gets the width of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle"""
            self.__height = value

        @property
        def x(self):
            """Gets the x coordinate of the rectangel"""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets the x coordinate of the new rectangle"""
            self.__x = value

        @property
        def y(self):
            """Gets the y coordinate for the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets the y coordinate for teh rectangle"""
            self.__x = value
