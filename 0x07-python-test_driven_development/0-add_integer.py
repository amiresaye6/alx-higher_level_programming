#!/usr/bin/python3
"""
this is a simpor add function to practes on testing modules by my self
"""
def add_integer(a, b=98):
    """
    adding two integer or float numbers
    Returns: intger value
    """


    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
