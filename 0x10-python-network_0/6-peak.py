#!/usr/bin/python3
"""
this module contains a function that finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers.
    """
    if (list_of_integers is None or len(list_of_integers) < 1):
        return None

    length = len(list_of_integers)
    start = 0
    mid = int(((length - start) // 2) + start)

    if (length == 1):
        return (list_of_integers[0])
    if (length == 2):
        return max(list_of_integers)

    if (list_of_integers[0] > list_of_integers[1] and
            list_of_integers[0] >= 0):
        return list_of_integers[0]

    if (list_of_integers[mid] >= list_of_integers[mid - 1] and
            list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
