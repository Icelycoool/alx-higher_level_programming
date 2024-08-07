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

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
