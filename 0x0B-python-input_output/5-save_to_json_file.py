#!/usr/bin/python3
"""
Module that writes an Object to a text file, using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file.

    Args:
        my_object: The object to be converted to JSON string representation.
        filename: The file to write the JSON to.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
