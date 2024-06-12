#!/usr/bin/python3
"""Module is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check if the object is an instance of.

    Returns:
        True: If the object is an instance of the given class or it's subclass.
        False: If the object isn't an instance of the given class or it's
        subclass.
    """
    return isinstance(obj, a_class)
