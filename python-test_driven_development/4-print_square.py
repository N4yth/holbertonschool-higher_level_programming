#!/usr/bin/python3

"""
4-print_square.py
this module contain a function that create a square made of '#'
"""


def print_square(size):
    """
    Create a square of '#'
    """
    if (not isinstance(size, int)):
        raise TypeError ("size must be an integer")
    if (size < 0):
        raise ValueError  ("size must be >= 0")
    for row in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print("")