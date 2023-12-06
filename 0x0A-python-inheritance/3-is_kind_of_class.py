#!/usr/bin/python3
"""checks if the object is the instance of the class
or the inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is the instance of class
    or a class that class in question inherits from
    """
    return (isinstance(obj, a_class))
