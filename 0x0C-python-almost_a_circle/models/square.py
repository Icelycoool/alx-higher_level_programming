#!/usr/bin/python3
"""Defines a square class."""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square instance.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes with the provided arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: A double pointer to a key/value for attributes to update.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args[:len(attrs)]):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
