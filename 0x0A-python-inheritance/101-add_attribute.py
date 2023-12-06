#!/usr/bin/python3
"""a module defines the function which adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add the new attribute to the object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
