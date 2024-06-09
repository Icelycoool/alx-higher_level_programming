#!/usr/bin/python3
"""Module lazy_matrix
Multiplies two matrices using MunPy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: list of lists of integers or floats
        m_b: list of lists of integers or floats

    Returns:
        The result of multiplying m_a by m_b
    """

    return numpy.matmul(m_a, m_b)
