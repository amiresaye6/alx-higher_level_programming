#!/usr/bin/python3
"""
module for class MyInt version 1
"""


class MyInt(int):
    """class inherited from int class"""

    def __eq__(self, other):
        """inverted equal"""
        if isinstance(other, MyInt):
            return not super().__eq__(other)
        return True

    def __ne__(self, other):
        """equal operator"""
        return not self.__eq__(other)
