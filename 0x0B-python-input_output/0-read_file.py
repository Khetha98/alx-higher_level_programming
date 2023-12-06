#!/usr/bin/python3
"""This module defines the text file-reading function"""


def read_file(filename=""):
    """Prints contents of the UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
