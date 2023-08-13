#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a + (0, 0)
    second = tuple_b + (0, 0)
    a = first[0] + second[0]
    b = first[1] + second[1]
    return a, b
