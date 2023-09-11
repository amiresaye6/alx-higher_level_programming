#!/usr/bin/python3
"""this is a modluel :)_"""


def add_attribute(obj, name, val):
    if (hasattr(obj, '__dict__')):
        setattr(obj, name, val)
    else:
        raise TypeError("can't add new attribute")
