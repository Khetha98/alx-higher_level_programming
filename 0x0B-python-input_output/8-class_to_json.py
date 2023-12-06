#!/usr/bin/python3
"""This module defines the Python class-to-JSON function"""


def class_to_json(obj):
    """Returns a dictionary representation of the simple data structure"""
    return obj.__dict__
