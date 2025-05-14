#!/usr/bin/python3

"""
5-text_indentation.py
this module contain a function that create a square made of '#'
"""


def text_indentation(text):
    """
    print a square of '#'
    Args:
        size (int): the size of the square
    """
    new_line = True
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for char in text:
        if (char == '.' or char == '?' or char == ':'):
            print("{}\n".format(char))
            new_line = True
        else:
            if (new_line == True and char.isspace()):
                continue
            new_line = False
            print(char, end="")
