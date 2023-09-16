#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json


class Base():
    """
    parent of all classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init the class
        Args:
            id (int): identifier for each instance of the class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
        Args:
            list_dictionaries (list): list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        Args:
            list_objs (list): list of instances who inherits of Base
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as file_w:
            if list_objs is None:
                file_w.write("")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file_w.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        Args:
            json_string (str): a string representing a list of dictionaries
            
        """

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        Args:
            dictionary (dict): a double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances:
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r", encoding="utf-8") as file_r:
                list_dict = Base.from_json_string(file_r.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        
        """
