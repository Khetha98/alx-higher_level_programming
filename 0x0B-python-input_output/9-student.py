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

    def to_json(self):
        """Gets the dictionary representation of a Student"""
        return self.__dict__
