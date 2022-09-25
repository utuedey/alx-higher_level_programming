#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for char in string_list:
        if char.lower() == 'c':
            idx = string_list.index(char)
            del string_list[idx]
            my_string = ''.join(string_list)
    return my_string
