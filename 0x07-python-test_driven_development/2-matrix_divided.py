#!/usr/bin/python3
"""
this module contains matrix_divided function
the matrics should have the same length of each row
it should be a list of lists containning intgers or float numerics
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    div: int to devide with, shouldnt be 0
    Returns: new matrics with all values devided by div
    """

    l1 = len(matrix)
    l2 = len(matrix[0])
    r = 0
    c = 0

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif len(row) != l2:
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
    new_matrics = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrics
