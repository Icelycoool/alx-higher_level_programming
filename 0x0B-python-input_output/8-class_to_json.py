#!/usr/bin/python3
"""
Module that Converts a Clas to JSON
"""


def class_to_json(obj):
    """
     Returns the dictionary description with simple data structure
     (list, dictionary, string, integer and boolean) for JSON
     serialization of an object.
    """
    if not hasattr(obj, "__dict__"):
        return {}
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
