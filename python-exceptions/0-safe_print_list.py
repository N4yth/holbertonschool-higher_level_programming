#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    resu = ""
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            resu += str(my_list[i])
        except IndexError:
            i -= 1
            break
    print("")
    return (i + 1)
