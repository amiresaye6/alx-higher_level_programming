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
    def __lt__(self, other):
        """Compare if square is less than another by area
        Args:
            other (Square): the other square to compare with
        Returns:
            True , False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area
        Args:
            other (Square): the other square to compare with
        Returns:
            True , False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other (Square): the other square to compare with
        Returns:
            True , False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): the other square to compare with
        Returns:
            True , False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): the other square to compare with
        Returns:
            True , False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): the other square to compare with
        Returns:
            True , False
        """
        return self.size > other.size
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
