#!/usr/bin/python3
"""
Module 100-matrix_mul
Contains method that does matrix multiplication
Requires same size lists/rows of ints or floats
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the result.

    Parameters:
    m_a (list): The first matrix.
    m_b (list): The second matrix.

    Returns:
    list: The result of the matrix multiplication.

    Raises:
    TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list of lists,
               or if one element of the matrices is not an integer or a float,
               or if the rows of m_a or m_b are not of the same size.
    ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")
    
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a) else "m_b must be a list of lists")

    # Check if m_a and m_b are empty
    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty" if len(m_a) == 0 else "m_b can't be empty")

    # Check if all elements of m_a and m_b are integers or floats
    for row in m_a:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if all rows of m_a and m_b have the same size
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_a[0])):
                sum += m_a[i][k] * m_b[k][j]
            row_result.append(sum)
        result.append(row_result)

    return result

