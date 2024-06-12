#!/usr/bin/python3
"""Module add_attribute"""


def add_attribute(obj, attr, val):
    """"
    Adds a new attribute to the given object.

    Parameters:
        obj: The object to which the attribute will be added.
        attr: The name of the attribute.
        val: The value of the attribute.

    Raises:
        TypeError:
            If the object does not support adding new attributes.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
