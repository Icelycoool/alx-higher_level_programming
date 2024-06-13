#!/usr/bin/python3
"""
Module that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text_file(UTF8) and prints it to stdout

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
