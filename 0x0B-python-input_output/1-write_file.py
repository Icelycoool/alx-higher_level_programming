#!/usr/bin/python3
"""
Module that writes a string to a text file (UTF8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file.

    Args:
        filename (str): The file to write to.
        text (str): The text to write / append to the file.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
