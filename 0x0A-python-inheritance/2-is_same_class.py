#!/usr/bin/python3
"""Checks whether object is the instance of the class"""


def is_same_class(obj, a_class):
    """Return true when object is the instance of a
    class, otherwise will return false
    """
    return (type(obj) == a_class)
