#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 2):
        tmp_list = list(tuple_a)
        for i in range(len(tuple_a), 3):
            tmp_list.append(0)
        tuple_a = tuple(tmp_list)
    if (len(tuple_b) < 2):
        tmp_list = list(tuple_b)
        for i in range(len(tuple_b), 3):
            tmp_list.append(0)
        tuple_b = tuple(tmp_list)
    res_tuple=(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (res_tuple)
