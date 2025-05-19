#!/usr/bin/python3

"""
module that create a square class
"""


class Square(object):
    """
    a class that represente square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ methode

        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = size
        if (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(position[0], int)and not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = position

    @property
    def size(self):
        """
        methode that return the actual size
        """
        return self._Square__size

    @property
    def position(self):
        """
        methode that return the actual position
        """
        return self._position

    @size.setter
    def size(self, value):
        """
        methode to set a new size

        Args:
            value (int): The new size
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @position.setter
    def position(self, value):
        """
        methode to set a new position

        Args:
            value (tuple): The new position
        """
        if (not isinstance(_position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(_position[0], int)and not isinstance(_position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (_position[0] < 0 or _position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(_position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        methode that return the area of the square
        """
        return (self._Square__size * self._Square__size)

    def my_print(self):
        """
        methode that print the square with the position and the width
        """
        if (self._Square__size == 0):
            print("")
        else:
            for row in range(0, self._Square__size):
                for column in range(0, self._Square__size):
                    if (column == 0):
                        for i in range(0, self._position[0]):
                            if self._position[1] > 0:
                                print("_", end="")
                            else:
                                print(" ", end="")
                    print("#", end="")
                print("")
