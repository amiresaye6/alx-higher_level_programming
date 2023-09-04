#!/usr/bin/python3
"""
A NEW MODULE ABOUT USLESS FUNCTION SO FAR
lets preted like it is usful to the society
"""


def print_square(size):
    """
    function print_square prnits a square to the terminal with the size length
    it returns nothing but raises some exceptions if invalid input is passed
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
    if size == 0:
        print()
