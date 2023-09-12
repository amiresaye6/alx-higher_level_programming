#!/usr/bin/python3
"""file input / output"""


def append_write(filename="", text=""):
    """append to the file"""

    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
