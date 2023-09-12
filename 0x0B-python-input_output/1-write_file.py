#!/usr/bin/python3
"""file input / output"""


def write_file(filename="", text=""):
    """writes text to a file"""

    with open(filename, "w", encoding="utf-8") as a:
        return a.write(text)
