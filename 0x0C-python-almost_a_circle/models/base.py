#!/usr/bin/python3
"""
Module that defines a base class
"""
import os
import json
import csv
import turtle


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

    @staticmethod
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

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of dictionaries from a JSON string representation.

            Args:
                json_string (str): A JSON string representation of a
                list of dictionaries.

            Returns:
                list: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary (dict): A dictionary of attributes to set.

        Returns:
            Base: An instance of the class with attributes set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                temp = cls(1, 1)
            else:
                temp = cls(1)
            temp.update(**dictionary)
            return temp

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Returns JSON string representation of  list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherit from Base.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: List of instances of the class.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_string = f.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherit from Base.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a CSV file.

        Returns:
            list: List of instances of the class.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in row.items())
                              for row in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(1)

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.forward(rectangle.width)
            t.right(90)
            t.forward(rectangle.height)
            t.right(90)
            t.forward(rectangle.width)
            t.right(90)
            t.forward(rectangle.height)
            t.right(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)
        t.hideturtle()
        turtle.done()
