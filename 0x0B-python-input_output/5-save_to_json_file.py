#!/usr/bin/python3
import json

to_json_string = __import__('3-to_json_string').to_json_string
"""
Module that writes an Object to a text file, using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file.

    Args:
        my_object: The object to be converted to JSON string representation.
        filename: The file to write the JSON to.
    """
    my_obj_JSON = to_json_string(my_obj)
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(my_obj_JSON)

