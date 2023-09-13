#!/usr/bin/python3
"""
Student class v 3
talking about nonsenc
"""


class Student():
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if type(attrs) == list:
            for attr in attrs:
                if not isinstance(attr, str):
                    return self.__dict__
            return{k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
