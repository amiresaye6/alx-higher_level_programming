#!/usr/bin/python3
"""
module for class Rectangle version 1
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """initial function"""

        BaseGeometry.__init__(self)
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
