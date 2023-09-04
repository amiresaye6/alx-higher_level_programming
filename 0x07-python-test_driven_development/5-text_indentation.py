#!/usr/bin/python3
"""
this module contain a function <text_indentation>
function that prints a text with 2 new lines after each of these characters:
 ., ? and :

"""


def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError exception
    with the message "text must be a string".
    There should be no space at the beginning or at the end
    of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    bad_space = 0
    for char in text:
        if bad_space == 0 and char == ' ':
            continue
        else:
            bad_space = 1

        if bad_space == 1:
            if char in [".", "?", ":"]:
                print(char, end="\n\n")
                bad_space = 0
            else:
                print(char, end="")
