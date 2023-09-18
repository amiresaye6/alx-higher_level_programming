#!/usr/bin/python3
"""square class version 1"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square.
        Args:
            size (int): square side length
            x (int): square x dimention
            y (int): square y dimention
            id (int): square id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        gettr function for size
        Returns:
            the __size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        setter for size
        Args:
            size (int): set the size with the value
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute:
        Args:
            args (int):
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            kwargs (dict):
                dictenaury with key : value
        """
        if args and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        dictionary representation of class Square
        """

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        string representation of the class Square
        Returns:
            string representation (str)
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
