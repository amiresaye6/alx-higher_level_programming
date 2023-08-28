#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = [0] * list_length
    for index in range(list_length):
        try:
            temp = my_list_1[index] / my_list_2[index]
        except IndexError:
            temp = 0
            print("out of range")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except ValueError:
            temp = 0
            print("wrong type")
        finally:
            res[index] = temp

    return res
