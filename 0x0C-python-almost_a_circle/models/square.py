#!/usr/bin/python3
"""It a module that ha square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """It a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """It a constructor"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Is a format for string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Square size setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """updates the square
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
        
    def to_dictionary(self):
        """it retruns out a dictonary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
