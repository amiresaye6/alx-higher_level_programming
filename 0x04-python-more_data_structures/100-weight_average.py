#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0
    div = 0
    for i in my_list:
        a, b = i
        res += a * b
        div += b
    return res / div
