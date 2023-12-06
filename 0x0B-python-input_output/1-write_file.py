#!/usr/bin/python3
"""This module defines the file-writing function."""


def write_file(filename="", text=""):
    """Writes the string to UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
