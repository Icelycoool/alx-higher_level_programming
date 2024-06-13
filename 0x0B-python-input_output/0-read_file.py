#!/usr/bin/python3
"""Module read_file"""


def read_file(filename=""):
    """
    Reads a text_file(UTF8) and prints it to stdout

    Args:
        filname (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
