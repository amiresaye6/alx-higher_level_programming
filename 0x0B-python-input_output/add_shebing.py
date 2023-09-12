#!/usr/bin/python3
"""
adds shebing to the top of python files
it is my oreginal idea :)
"""


def add_shebang(filenames):
    """adds shebing to the start of a list of .py files"""

    for name in filenames:
        with open(name, "a", encoding="utf-8") as file:
            file.seek(0)
            file.write("#!/usr/bin/python3")
