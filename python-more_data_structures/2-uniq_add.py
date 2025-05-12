#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    for idx in range(0, len(my_list)):
        print(my_list[idx])
        if (my_list[idx] not in my_list[:idx]):
            result += my_list[idx]
    return (result)
