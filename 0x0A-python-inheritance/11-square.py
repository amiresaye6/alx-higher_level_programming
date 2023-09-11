#!/usr/bin/python3
"""
module for class square version 2
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class representation"""

    def __init__(self, size):
        """init function"""
        Rectangle.__init__(self, size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area"""
        return (self.__size ** 2)

    def __str__(self):
        """string representation of the class"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
