#!/usr/bin/python3
"""This module defines the file-appending function."""


def append_write(filename="", text=""):
    """Appends the string to end of the UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
