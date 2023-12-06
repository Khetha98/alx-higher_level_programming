#!/usr/bin/python3
"""This module defines the JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates the Python object from the given JSON file"""
    with open(filename) as k:
        return json.load(k)
