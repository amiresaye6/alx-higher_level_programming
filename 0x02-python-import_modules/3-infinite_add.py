#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for i, arg in enumerate(sys.argv[1:], start=1):
        sum += int(arg)
    print("{}".format(sum))
