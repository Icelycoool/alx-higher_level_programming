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

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
