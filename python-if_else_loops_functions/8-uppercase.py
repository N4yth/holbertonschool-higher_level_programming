#!/usr/bin/python3

def uppercase(str):
    final_str = ""
    for i in range(len(str)):
        asc = ord(str[i])
        if (asc > 96 and asc < 123):
            final_str += "{:c}".format(asc - 32)
        else:
            final_str += str[i]
    print(final_str)
    return False
