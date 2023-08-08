#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if ord(i) <= 97 or ord(i) >= 122:
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{}".format(res))
