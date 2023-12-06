#!/usr/bin/python3
"""This module defines the class Student"""


class Student:
    """Represent the student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets the dictionary representation of a Student.
        If attrs is the list of strings, represents only the attributes
        included on the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all the attributes of a Student
        """
        for k, v in json.items():
            setattr(self, k, v)
