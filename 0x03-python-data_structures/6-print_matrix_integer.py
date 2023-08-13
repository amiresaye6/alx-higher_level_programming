#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # if matrix == [[""]]:
    #     print()
    for row in matrix:
        for index, item in enumerate(row):
            if index == len(row) - 1:
                print("{:d}".format(item), end="")
                continue
            print("{:d}".format(item), end=" ")
        print()
