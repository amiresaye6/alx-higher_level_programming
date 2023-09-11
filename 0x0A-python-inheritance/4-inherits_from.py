#!/usr/bin/python3
"""
module check for instances
"""


def inherits_from(obj, a_class):
    """returns True if instance and False otherwise"""

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
