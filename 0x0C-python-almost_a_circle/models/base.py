#!/usr/bin/python3

import json
import os

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """It returns the JSON representation of list_dictionaries"""

        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)



    @staticmethod
    def from_json_string(json_string):
        """It returns list of JSON string representations"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list


    @classmethod
    def save_to_file(cls, list_objs):
        """Save the string object into a file"""

        file = cls.__name__ + ".json"
        with open(file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                lists = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(lists))


    @classmethod
    def create(cls, **dictionary):
        """Gives out an instance with its attributes"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        """Loads dictionary that represents
        parameters for instance and then
        creates instances"""
        file = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file):
            with open(file, 'r') as my_file:
                my_string = my_file.read()
                list_dictionaries = cls.from_json_string(my_string)
                for dicti in list_dictionaries:
                    list_of_instances.append(cls.create(**dicti))
        return list_of_instances
