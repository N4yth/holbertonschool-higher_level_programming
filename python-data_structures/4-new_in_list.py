#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cpy_list = []
    if (idx < 0 or idx > len(my_list) - 1):
        return (my_list)
    for i in range(0, len(my_list)):
        cpy_list.append(my_list[i])
    cpy_list[idx] = element
    return (cpy_list)
