#!/usr/bin/python3
"""
unit test file for square module and its Square class
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    class for testing Rectangle class in rectangle model
    """

    def test_module_documentation(self):
        """
        test checks for module documentation
        """

        module = Square.__module__.__doc__
        self.assertTrue(len(module) > 1)

    def test_class_documentation(self):
        """
        test checks for class documentation
        """

        function_ = Square.__doc__
        self.assertTrue(len(function_) > 1)

    def test_First_Square(self):
        """
        test First Rectangle
        """

        r1 = Square(10)
        self.assertTrue(r1.id > 0)

        r2 = Square(2)
        self.assertTrue(r2.id > r1.id)

    def test_Validate_attributes_1(self):
        """
        test Validate attributes
        """
        with self.assertRaises(TypeError):
            Square(10, "2")

    def test_Validate_attributes_2(self):
        """
        test Validate attributes
        """
        with self.assertRaises(ValueError):
            r = Square(10)
            r.width = -10

    def test_Validate_attributes_3(self):
        """
        test Validate attributes
        """
        with self.assertRaises(TypeError):
            r = Square(10)
            r.x = {}

    def test_Validate_attributes_4(self):
        """
        test Validate attributes
        """
        with self.assertRaises(TypeError):
            r = Square(10)
            r.x = {}

    def test_Area_first(self):
        """
        test Area first
        """
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

        r2 = Square(2)
        self.assertEqual(r2.area(), 4)

    def test_Display_0(self):
        """
        test Display #0
        """

        r1 = Square(4, 6)
        self.assertEqual(r1.display(), None)

        r2 = Square(5, 10)
        self.assertEqual(r2.display(), None)

    def test_str(self):
        """
        test __str__ magic function
        """

        r1 = Square(4, 2, 1, 12)
        self.assertNotEqual(r1, None)

        r2 = Square(5, 5, 1)
        self.assertNotEqual(r2, None)


if __name__ == "__main__":
    unittest.main()
