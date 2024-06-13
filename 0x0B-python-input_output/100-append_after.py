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
    # Initialize an empty string to store the modified content
    content = ""

    # Open the file in read mode
    with open(filename) as f:
        # Iterate through each line in the file and append it to content
        for line in f:
            content += line

            # if search_string is in line append it to the content
            if search_string in line:
                content += new_string

    # Reopen the file in write mode
    with open(filename, "w") as f:
        # Write the modified content back to the file
        f.write(content)
