#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or len(str) == 0:
        return str
    res = ""
    for i in range(len(str)):
        if i == n:
            continue
        res += str[i]
    return res
