#!/usr/bin/python3
"""Module is_same_class"""


def is_same_class(obj, a_class):
    """
    Checks if an objects is an exact instance of a given class.

    Args:
        object: The object to be checked.
        a_class: The class to check if the object is part

    Returns:
        True: If the object if an instance of the given class.
        False: If the object is not an exact instance of the given class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
