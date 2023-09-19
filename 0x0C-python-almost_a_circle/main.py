#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

if __name__ == "__main__":
    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
