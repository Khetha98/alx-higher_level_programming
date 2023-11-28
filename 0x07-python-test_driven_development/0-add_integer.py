#!/usr/bin/python3
"""

This module has the function that adds up 2 integers

"""


def add_integer(a, b=98):
    """ It returns the sum of two integers

    Args:
        a: one argument
        b: second argument

    Returns:
        the sum of two arguments inputs

    Raises:
        TypeError: If one of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
