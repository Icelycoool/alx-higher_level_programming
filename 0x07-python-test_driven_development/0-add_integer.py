#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if they are floats.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float. Default is 98.

    Returns:
        The sum of a and b, casted to integers if necessary.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
