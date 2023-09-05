#!/usr/bin/python3

"""
this module is the fourth version of the class Rectangle
"""


class Rectangle():
    """
    simple Rectangle class
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width with value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height with value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function returns the area of the Rectangle opgect"""
        return self.__width * self.__height

    def perimeter(self):
        """function returns ther perimeter of the Rectangle opgect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the rectangle as a string of '#' """
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for _ in range(self.__height):
            output += "#" * self.__width
            if _ < self.__height - 1:
                output += "\n"
        return output

    def __repr__(self):
        """returns string representation of Rectange"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """runs before the destruction of the opgect"""
        print("Bye rectangle...")
