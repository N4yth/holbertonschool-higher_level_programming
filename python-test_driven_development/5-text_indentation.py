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
    Line = ""
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for char in text:
        Line += char
        if char in ".:?":
            print(Line.strip())
            print()
            Line = ""
    if Line.strip():
        print(Line.strip(), end="")
