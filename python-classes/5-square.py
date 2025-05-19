#!/usr/bin/python3

"""
module that create a square class
"""


class Square(object):
    """
    a class that represente square
    """
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = size

    @property
    def size(self):
        """
        methode that return the size
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        methode set a new size
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        methode that return the area of the square
        """
        return (self._Square__size * self._Square__size)

    def my_print(self):
        """
        methode that print the square
        """
        if (self._Square__size == 0):
            print("")
        else:
            for row in range(0, self._Square__size):
                for column in range(0, self._Square__size):
                    print("#", end="")
                print("")
