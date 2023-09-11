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
r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
