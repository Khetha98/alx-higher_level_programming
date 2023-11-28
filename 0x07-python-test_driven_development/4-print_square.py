#!/usr/bin/python3

"""

The module has a function which prints the square

"""

def print_square(size):
    """This function prints the square with character #

    Args:
        size: This represents a length of square

    Raises:
        TypeError: when size is not the integer
        TypeError: when size is the float and less than zero
        ValueError: when size is less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
