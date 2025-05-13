#!/usr/bin/python3

"""
2-matrix_divided.py
this module divide all number of a matrix by a given
number
"""


def matrix_divided(matrix, div):
    """
    devided all number of a matrix by a given data
    """
    new_matrix = []
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for row in range(0, len(matrix) - 1):
        if (len(matrix[row]) != len(matrix[row + 1])):
            raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        tmp_list = []
        for column in row:
            result = 0
            if (not isinstance(column, int) and not isinstance(column, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats")
            
            result = round(column / div, 2)
                
            tmp_list.append(result)
        new_matrix.append(tmp_list)
    return (new_matrix)
