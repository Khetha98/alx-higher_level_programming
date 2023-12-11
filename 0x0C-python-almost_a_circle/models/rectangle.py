#!/usr/bin/python3
"""Module that has rectangle class"""

from models.base import Base


class Rectangle(Base):
    """It a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None): 
        """It a constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getters for each attribute
    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @property
    def height(self):
        """Getter for the height"""
        return self.__height

    @property
    def x(self):
        """Getter for the x"""
        return self.__x

    @property
    def y(self):
        """Gette for the y"""
        return self.__y

    # Setters for each attribute
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines area of a rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """displays the rectangle in # format"""
        for i in range(self.y):
            print("")
        for j in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """The format for the string representation for the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"


    def update(self, *args, **kwargs):
        """Assigns the argument to each attribute"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass


    def to_dictionary(self):
        """
            It returns a dictionary representation of this class
        """

        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
