#!/usr/bin/python3

def no_c(my_string):
    cpy_list = ""
    for i in my_string:
        if (i != 'c' and i != 'C'):
            cpy_list += i
    my_string = cpy_list
    return (my_string)
