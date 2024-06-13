#!/usr/bin/python3
"""
Module that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each
    line containing a specific string.

    Args:
        filename: The file to insert the text to.
        search_string (str): The string to be searched for in each line.
        new_string (str): The string to be inserted after the line
                            containing search_string.
    """
    with open(filename, "r+", encoding="UTF-8") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)

        f.seek(0)

        f.writelines(lines)
