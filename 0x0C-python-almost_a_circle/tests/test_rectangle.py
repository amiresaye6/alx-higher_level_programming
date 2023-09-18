#!/usr/bin/python3
"""
unit test file for base module and its Base class
"""
import unittest
from models.rectangle import Rectangle



class TestRectangleClass(unittest.TestCase):
    """
    class for testing Rectangle class in rectangle model
    """

    def test_module_documentation(self):
        """
        test checks for module documentation
        """

        module = Rectangle.__module__.__doc__
        self.assertTrue(len(module) > 1)

    def test_class_documentation(self):
        """
        test checks for class documentation
        """

        function_ = Rectangle.__doc__
        self.assertTrue(len(function_) > 1)

    def test_First_Rectangle(self):
        """
        test First Rectangle
        """

        r1 = Rectangle(10, 2)
        self.assertTrue(r1.id > 0)

        r2 = Rectangle(2, 10)
        self.assertTrue(r2.id > r1.id)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertTrue(r3.id > r2.id)

    def test_Validate_attributes_1(self):
        """
        test Validate attributes
        """
        with self.assertRaises(TypeError):
             Rectangle(10, "2")

    def test_Validate_attributes_2(self):
        """
        test Validate attributes
        """
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

    def test_Validate_attributes_3(self):
        """
        test Validate attributes
        """
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

    def test_Validate_attributes_4(self):
        """
        test Validate attributes
        """
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

    def test_Area_first(self):
        """
        test Area first
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_Display_0(self):
        """
        test Display #0
        """

        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), None)

        r2 = Rectangle(5, 10)
        self.assertEqual(r2.display(), None)

    def test_str(self):
        """
        test __str__ magic function
        """

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertNotEqual(r1, None)

        r2 = Rectangle(5, 5, 1)
        self.assertNotEqual(r2, None)


if __name__ == "__main__":
    unittest.main()
