#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keyes = []
    for key, item in a_dictionary.items():
        if item == value:
            keyes.append(key)
    for key in keyes:
        del a_dictionary[key]
    return a_dictionary
