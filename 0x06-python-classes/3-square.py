#!/usr/bin/python3
"""
this is square class
"""


class Square:
    """
    square class
    Attributes:
        __size (int): size of a side of the square
        area: function returns the area of the square
    """

    def __init__(self, size=0):
        """
        initializing a square
        Args:
            __size (int): size of a side of a square
        Returns: none
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        calculates the area of the the square
        Returns: the area
        """
        return self.__size * self.__size
