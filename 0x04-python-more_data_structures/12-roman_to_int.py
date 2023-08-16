#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    prev = 0
    for num in reversed(roman_string):
        if num not in roman_nums:
            return 0
        val = roman_nums[num]
        if val >= prev:
            res += val
        else:
            res -= val
        prev = val
    return res
