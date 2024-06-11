#!/usr/bin/python3
"""Module locked_class"""


class LockedClass:
    """
    A class that allows dynamic creation of the 'first_name' attribute

    The class uses the '__slot__' attribute to restrict creation of any instance
    attribute other than 'first_name'.

    Attributes:
        first_name (str):
            The only attribute that can be dynamically created.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initialized the LockedClass instance.
        """
        pass
