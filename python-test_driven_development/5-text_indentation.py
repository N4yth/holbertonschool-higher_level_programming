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
    for char in range(0,len(text)):
        if (text[char] == '.' or text[char] == '?' or text[char] == ':'):
            print("{}\n".format(text[char]))
            new_line = True
        else:
            if (new_line == True and text[char].isspace()):
                continue
            elif (text[char].isspace()):
                test = char
                while (text[test].isspace()):
                    test += 1
                    if (not text[test].isspace()):
                        break
                    else:
                        try:
                            text[test].isspace()
                        except IndexError:
                            return()
            new_line = False
            print(text[char], end="")
