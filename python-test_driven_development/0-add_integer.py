#!/usr/bin/python3

"""
0-add_integer.py
ce module contient une fonction qui permet de faire la somme de 2 entier
raise une exectpion cas de format non conforme
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(int(a) + int(b))
