#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(0, len(matrix)):
        new_matrix.append(list(map(square, matrix[row])))
    return (new_matrix)


def square(n):
    return (n * n)
