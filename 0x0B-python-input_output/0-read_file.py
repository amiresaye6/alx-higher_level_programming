#!/usr/bin/python3
"""file input / output"""


def read_file(filename=""):
    """reads and prints a file"""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
