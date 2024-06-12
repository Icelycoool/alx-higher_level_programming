#!/usr/bin/python3
"""Module inherits_from"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check if the object is an instance of.

    Returns:
        True: If the object is an instance of the given class or its subclass.
        False: If the object is not an instance of the given class
                or its subclass.
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
