#!/usr/bin/python3
"""
module for class square version 1
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
