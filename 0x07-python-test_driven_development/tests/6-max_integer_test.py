#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    class for testing max_intger function in 6-max_intger module
    """

    def test_module_documentation(self):
        """
        test checks for module documentation
        """

        module = __import__("6-max_integer").__doc__
        self.assertTrue(len(module) > 1)

    def test_function_documentation(self):
        """
        test checks for function documentation
        """

        function_ = max_integer.__doc__
        self.assertTrue(len(function_) > 1)

    def test_no_args(self):
        """
        test with no arugments passed
        """

        self.assertEqual(max_integer(), None)
        self.assertIsNone(max_integer([]))

    def test_valid_input(self):
        """
        test with valid list
        """

        input = [1, 2, 3, 4, 5, 60]
        self.assertEqual(max_integer(input), 60)
        input = [1, 2, -3, -4, 5, -60]
        self.assertEqual(max_integer(input), 5)


    def test_negative_valid_input(self):
        """
        test with negative valid list
        """

        input = [-1, -2, -3, -4, -5, -60]
        self.assertEqual(max_integer(input), -1)

    def test_all_zeros(self):
        """
        test with all values are zero
        """

        input_0 = [0, 0, 0, 0, 0, 0]
        self.assertEqual(max_integer(input_0), 0)

    def test_none(self):
        """
        Tests for passing none as argument
        """

        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
