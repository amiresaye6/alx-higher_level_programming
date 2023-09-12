#!/usr/bin/python3
"""
Student class v 2
"""


class Student():
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """init func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if type(attrs) == list:
            return self.__dict__ in attrs
        return self.__dict__
