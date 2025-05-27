#!/usr/bin/python3
"""
this module have class 
"""

from abc import ABC, abstractmethod
import math



class Shape(ABC):
    """
    this is the abstract class
    """
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """
    this is the Circle class
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        the methode that return the area of the circle
        """
        return (math.pi * (self.radius ** 2))

    def perimeter(self):
        """
        the methode that return the perimeter of the circle
        """
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    this is the Rectangle class
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        the methode that return the area of the Rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        the methode that return the perimeter of the Rectangle
        """
        return ((self.width + self.height) * 2)


def shape_info(forme):
    """
    the methode use to display the area and the perimeter
    """
    print("Area: {}".format(forme.area()))
    print("Perimeter: {}".format(forme.perimeter()))
