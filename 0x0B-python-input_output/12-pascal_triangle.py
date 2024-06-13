#!/usr/bin/python3
"""
Module that creates pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to be generated.

    Returns:
        list of list: A list of lists representing Pascal's Triangle.
    """
    # If n is less than or equal to 0 return an empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Create a new row initialized with 1
        row = [1] * (i + 1)

        # Add the correct inner value for each row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Add the row to the triangle
        triangle.append(row)

    return triangle
