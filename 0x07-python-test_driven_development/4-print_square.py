#!/usr/bin/python3
"""Module print_square"""


def print_square(size):
    """
    Prints a square using the character `#`.

    Args:
        size (int): size of the square's sides.

    Raises:
        TypeError: If `size` is not integer.
        ValuError: If `size` is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
