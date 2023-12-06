#!/usr/bin/python3
"""This module inherits the list class"""


class MyList(list):
    """A class that inherits the list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
