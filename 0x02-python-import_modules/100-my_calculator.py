#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[1])
    result = 0
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
