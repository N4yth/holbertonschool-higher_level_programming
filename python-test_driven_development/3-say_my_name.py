#!/usr/bin/python3

"""
3-say_my_name.py
this module divide all number of a matrix by a given
number
"""


def say_my_name(first_name, last_name=""):
    """
    print a given name
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
