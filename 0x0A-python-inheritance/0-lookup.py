#!/usr/bin/python3
"""Module lookup"""


def lookup(object):
    """"
    Returns the list of available attributes and methods of an object.

    Args:
        object: The object to inspect.

    Returns:
        List[str]: A list of strings representing the names of
        the attributes and methods of the object.
    """
    return dir(object)
