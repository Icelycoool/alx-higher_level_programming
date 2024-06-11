#!/usr/bin/python3
"""Module my_list"""


class MyList(list):
    """
    Inherits from list class.

    Methods:
        print_sorted(self): Prints the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
