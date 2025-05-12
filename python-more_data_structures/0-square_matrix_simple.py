#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = lambda a : a * a
    for row in range(0, len(matrix)):
        new_matrix.append(list(map(square, matrix[row])))
    return (new_matrix)