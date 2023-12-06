#!/usr/bin/python3
"""This module defines the JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns Python object representation of the JSON string"""
    return json.loads(my_str)
