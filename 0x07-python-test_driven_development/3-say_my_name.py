#!/usr/bin/python3

"""

The module have a function that prints the name

"""

def say_my_name(first_name, last_name=""):
    '''This function prints the name

    Args:
        first_name: fisrt name to be printed
        last_name: last name to be printed

    Raises:
        TypeError: If either one of parameters are not strings

    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
