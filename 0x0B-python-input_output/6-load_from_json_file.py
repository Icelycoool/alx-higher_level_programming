#!/usr/bin/python3
"""
Module that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Creates objects from JSON file.

    Args:
        filename: The file to be converted to an object.

    Returns:
        obj: Python object representing the JSON data.
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
