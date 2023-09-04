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

    l2 = len(matrix[0])
    err_massage = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(err_massage)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_massage)

        elif len(row) != l2:
            raise TypeError(
                "Each row of the matrix must have the same size"
                )

        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(err_massage)

    new_matrics = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrics
