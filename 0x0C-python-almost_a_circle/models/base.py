#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json


class Base():
    """
    parent of all classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init the class
        Args:
            id (int): identifier for each instance of the class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
