#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    the_max = my_list[0]
    for i in my_list:
        if the_max < i:
            the_max = i
    return the_max
