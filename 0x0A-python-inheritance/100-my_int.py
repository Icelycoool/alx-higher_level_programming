#!/usr/bin/python3
"""Module MyInt"""


class MyInt(int):
    """Class that inherits from int with inverted == and != operators"""

    def __eq__(self, other):
        """Overides the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator"""
        return super().__eq__(other)
