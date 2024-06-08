#!/usr/bin/python3
"""Module matrix_mul"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of multiplying m_a and m_b.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists,
                   if any element of m_a or m_b is not an integer or a float,
                   or if any row of m_a or m_b has different lengths.
        ValueError: If m_a or m_b is empty,
                    or if the number of columns in m_a is not equal to
                    the number of rows in m_b.
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

    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            element_sum = 0
            for k in range(num_columns_a):
                element_sum += m_a[i][k] * m_b[k][j]
            result_row.append(element_sum)
        result.append(result_row)

    return result
