#!/usr/bin/python3
"""
Module that returns an object (Python data structure)
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string to a python object.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        obj: Python object representing the JSON string.
    """
    return json.loads(my_str)
