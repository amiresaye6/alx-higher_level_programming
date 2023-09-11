#!/usr/bin/python3
"""
module for class BaseGeometry version 3
"""


class BaseGeometry():
    """this is a class ()__()"""

    def __init__(self):
        """
        initialization function
        """
        pass

    def area(self):
        """raisesa an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks for validation"""

        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))

        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
