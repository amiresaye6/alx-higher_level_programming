#!/usr/bin/python3
"""
unit test file for base module and its Base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    class for testing Base class in base model
    """

    def test_module_documentation(self):
        """
        test checks for module documentation
        """

        module = Base.__module__.__doc__
        self.assertTrue(len(module) > 1)

    def test_class_documentation(self):
        """
        test checks for class documentation
        """

        function_ = Base.__doc__
        self.assertTrue(len(function_) > 1)

    def test_Base_class(self):
        """
        test Base class
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
