#!/usr/bin/python3
"""
simple modeule to print a single phrase
raises some error massages
say my name
"""


def say_my_name(first_name, last_name=""):
    """
    prints "My name is "firs_name" "last_name"
    RETURNS NONE
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
