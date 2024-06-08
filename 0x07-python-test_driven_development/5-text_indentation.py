#!/usr/bin/python3
"""Mode text_indentation

This module provides a function `text_indentation` that prints a 
text with 2  new lines after the following characters `.`, `?` and `:`
"""


def text_indentation(text):
    """
    Prints text with two new lines after `.`, `?` and `:`.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join(
                [line.strip(" ") for line in text.split(char)])

    print("{}".format(text), end="")
