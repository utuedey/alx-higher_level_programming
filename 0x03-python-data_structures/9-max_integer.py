#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_number = my_list[0]
        for number in range(len(my_list)):
            if my_list[number] > max_number:
                max_number = my_list[number]
        return max_number
