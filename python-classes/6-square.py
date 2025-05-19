#!/usr/bin/python3

"""
module that create a square class
"""


class Square(object):
    """
    a class that represente square
    """
    def __init__(self, size=0, position=(0, 0)):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = size
        if (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)and not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = position

    @property
    def size(self):
        """
        methode that return the actual size
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        """
        methode that return the actual position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[0], int)and not isinstance(value[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for line in range(0, self.__position[1]):
                print("")
            for row in range(0, self._Square__size):
                for column in range(0, self._Square__size):
                    if (column == 0):
                        for i in range(0, self.__position[0]):
                            print(" ", end="")
                    print("#", end="")
                print("")
