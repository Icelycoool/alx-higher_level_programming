#!/usr/bin/python3
"""
Module that defines a base class
"""
import json


class Base:
    """
    Base class for managing 'id' attribute of all instances.

    Attributes:
        __nb_objects (int): Class attribute that counts
                            the number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The id for the instance. If None, the
                        id is set to the next number in sequence.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
