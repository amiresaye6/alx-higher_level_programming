#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """
    triangle_res = []
    if n <= 0:
        return triangle_res
