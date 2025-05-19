#!/usr/bin/python3

"""
module that create a square class
"""


class Square:
    """
    a class that represente square
    """
    def __init__(self, size=0):
        self._Square__size = size
        if (not isinstance(self._Square__size, int)):
            raise TypeError("size must be an integer")
        if (self._Square__size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """
        function that return the area of the square
        """
        return (self._Square__size * self._Square__size)
