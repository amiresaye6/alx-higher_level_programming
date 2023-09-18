#!/usr/bin/python3
"""
class Rectangle version 1
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        Args:
            width (int): The the Rectangle width.
            heiht (int): The the Rectangle heiht.
            x (int): The the Rectangle x.
            y (int): The the Rectangle y.
            id (int): the id of the class object
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        gettr function for width
        Returns:
            the __width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter for width
        Args:
            width (int): set the width with the value
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        gettr function for height
        Returns:
            the __height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter for height
        Args:
            height (int): set the height with the value
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        gettr function for x
        Returns:
            the __x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter for x
        Args:
            x (int): set the x with the value
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        gettr function for y
        Returns:
            the __y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter for y
        Args:
            y (int): set the width y the value
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        calculate the area of Rectangle
        Returns:
            the area (int)
        """
        return self.__width * self.__height

    def display(self):
        """
        represent the Rectangle with (#)
        """
        char = "#"
        [print() for _ in range(self.__y)]
        for _ in range(self.__height):
            print(" " * self.__x + "{}".format(char) * self.__width)

    def __str__(self):
        """
        string representation of the class Rectangle
        Returns:
            string representation (str)
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute:
        Args:
            args (int):
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            kwargs (dict):
                dictenaury with key : value
        """
        if args and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(
                            self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x = arg
                elif index == 4:
                    self.__y = arg
                index += 1
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(
                            self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        dictionary representation of class Rectangle
        """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
