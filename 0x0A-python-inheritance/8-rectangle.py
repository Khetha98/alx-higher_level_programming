#!/usr/bin/python3
"""Inheris from the baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that define rectangle using the BaseGeometry"""

    def __init__(self, width, height):
        """Intialize the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
