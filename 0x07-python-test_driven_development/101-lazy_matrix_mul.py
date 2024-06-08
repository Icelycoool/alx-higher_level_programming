#!/usr/bin/python3
"""Module lazy_matrix
Multiplies two matrices using MunPy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: list of lists of integers or floats
        m_b: list of lists of integers or floats

    Returns:
        The result of multiplying m_a by m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    row_length_a = len(m_a[0])
    if not all(len(row) == row_length_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_length_b = len(m_b[0])
    if not all(len(row) == row_length_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    num_columns_a = len(m_a[0])
    num_rows_b = len(m_b)

    if num_columns_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
