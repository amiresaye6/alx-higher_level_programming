#!/usr/bin/python3
"""thie module is about the multiblication of matrix"""


def matrix_mul(m_a, m_b):
    """multibly matrix"""

    l_1 = len(m_a[0])
    l_2 = len(m_b[0])
    result = [[0 for _ in range(l_2)] for _ in range(len(m_a))]

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for _ in m_a:
        if not isinstance(_, list):
            raise TypeError("m_a must be a list of lists")
        for item in _:
            if type(item) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if len(_) != l_1:
            raise TypeError("each row of m_a must be of the same size")

    for _ in m_b:
        if not isinstance(_, list):
            raise TypeError("m_b must be a list of lists")
        for item in _:
            if type(item) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if len(_) != l_2:
            raise TypeError("each row of m_b must be of the same size")

    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")

    if m_a == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if l_1 != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        for j in range(l_2):
            for k in range(l_2):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
