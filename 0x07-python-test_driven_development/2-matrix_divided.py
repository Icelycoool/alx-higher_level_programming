#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        new_matrix: A new matrix divided by the divisor,
                    rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is empty, not list | (matrix / div)  not a number.
        ZeroDivisionError: If div is 0.
    """

    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not all(isinstance(row, list) and row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num/div, 2) for num in row] for row in matrix]
    return new_matrix
