#!/usr/bin/python3

"""
this module have a function that look if the object is
an instance of a given class
"""


def inherits_from(obj, a_class):
    """
    the function return true if the object is an instance
    of a class that inherited (direct or not) from
    the given class
    """
    if (type(obj) != a_class):
        return True
    return (not isinstance(obj, a_class))
