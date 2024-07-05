#!/usr/bin/python3
"""Module that finds the peak number"""


def find_peak(list_of_integers):

    """
    Function that finds a peak in a list

    Args:
        list_of_integers (list): The list of arguments to be checked.

    Returns:
        int : The peak integer in the list.
    """
    if not list_of_integers:
        return None

    return max(list_of_integers)
