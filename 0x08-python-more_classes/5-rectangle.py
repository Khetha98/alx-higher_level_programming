#!/usr/bin/python3
"""
This class defines a rectangle
"""


class Rectangle:
    """
    It a class that represents a rectangle
    """

    def __init__(self,  width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        getter
        '''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''
        setter
        '''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''
        getter
        '''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''
        setter
        '''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''
        return the area of rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        return the perimeter of perimeter
        '''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        '''
        return: the string representation of rectangle
        '''
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += '#' * self.width
            if idx + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def __repr__(self):
        '''
        return: representation of a rectangle that can be used by eval() to
                create new object
        '''
        ret_str = "Rectangle(" + str(self.__width) + ","
        ret_str += str(self.__height) + ")"
        return ret_str

    def __del__(self):
        '''
           deletes instance of a Rectangle class, and prints "bye" message
        '''
        print("Bye rectangle...")
