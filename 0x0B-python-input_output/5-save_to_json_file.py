#!/usr/bin/python3
"""This module defines the JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes the object to the text file using JSON format"""
    with open(filename, "w") as k:
        json.dump(my_obj, k)
