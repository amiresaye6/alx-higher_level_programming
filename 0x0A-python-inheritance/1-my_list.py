#!/usr/bin/python3
"""
MyList class module version 1
"""


class MyList(list):
    """
    class MyList inherits from list
    """

    def __init__(self):
        """initialize Mylist class"""
        super().__init__(self)

    def print_sorted(self):
        """prints the sorted list given"""
        print(sorted(self))
