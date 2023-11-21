#!/usr/bin/python3
# 0-square.py by Ehoneah Obed
"""This module defines a square """


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """Initializing a square class
        Args:
            size: represnets size of a square defined
        Raises:
            TypeError: if the size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of a square
        Returns: The square of size
        """

        return (self.__size ** 2)
