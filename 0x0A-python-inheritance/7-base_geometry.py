#!/usr/bin/python3
"""Defines the base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents the base geometry"""

    def area(self):
        """method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value as the integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
