#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json
import csv
import turtle


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
        serializes in CSV:
        Args:
            list_objs (list): list of objs to but in csv file
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", encoding="utf-8") as file_w:
            if not list_objs or len(list_objs) == 0:
                file_w.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file_w, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes in CSV:
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", encoding="utf-8") as file_r:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file_r, fieldnames=fields)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares:
        Args:
            list_rectangles (list):
            list_squares (list):
        """

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()

            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)

            turt.hideturtle()

        turt.color("#b5e3d8")

        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()

            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
