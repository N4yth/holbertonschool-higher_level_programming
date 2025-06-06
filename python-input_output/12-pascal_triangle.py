#!/usr/bin/python3

'''
This module contain 1 function
'''


def pascal_triangle(n):
    '''
    function that return the List of each row of the pascal triangle
    '''
    List = []
    if n <= 0:
        return List

    past_row = []
    row = []
    len_list = 1
    for y in range(0, n):
        for i in range(0, len_list):
            if i == 0 or i == len_list - 1:
                row.append(1)
            else:
                row.append(past_row[i - 1] + past_row[i])
        len_list += 1
        List.append(row[:])
        past_row = row[:]
        row = []
    return List
