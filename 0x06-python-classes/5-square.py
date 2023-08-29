#!/usr/bin/python3
"""
this is square class
"""


class Square:
    """
    square class
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """
        initializing a square
        Args:
            size (int): size of a side of a square
        Returns: none
        """
        self.size = size

    def area(self):
        """
        calculates the area of the the square
        Returns: the area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        gets the __size
        Returns: the __size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints the square in #s and plank line if size is 0
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
