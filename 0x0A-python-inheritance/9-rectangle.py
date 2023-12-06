#!/usr/bin/python3
"""Defines the class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class represents the rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize the new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of the Rectangle"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
