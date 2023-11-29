#!/usr/bin/python3
"""
This class defines a rectangle
"""


class Rectangle:
    """
    It a class that represents a rectangle
    """

    def __init__(self,  width=0, height=0):
        """
        Initializing the rectangle class
        Args:
            width: represents the width of a rectangle
            height: represents the height of a rectangle
        Raises:
            TypeError: if the size is not the integer
            ValueError: if size is less than value zero
        """
        
        self.width = width
        self.height = height

        @property
        def width(self):
            """retrieves width attribute"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets width attribute"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """retrieves height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
