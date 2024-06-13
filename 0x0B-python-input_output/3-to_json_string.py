#!/usr/bin/python3
"""
Module that returns the JSON representation of an object (string).
"""


import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Args:
        my_object : The object to be returned as JSON.

    Returns:
        str: The JSON representation of the object as a string
    """
    return json.dumps(my_obj)
