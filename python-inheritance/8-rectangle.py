#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
this module have a class of geometry
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("Rectangle", width)
        self.__width = width
        self.integer_validator("Rectangle", height)
        self.__height = height
