#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_multiple_int(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_int(self):
        self.assertEqual(max_integer([45]), 45)

    def test_negative_elements(self):
        self.assertEqual(max_integer([-4, -2, -3]), -2)

    def test_float(self):
        self.assertEqual(max_integer([1.0, 2.5, 7.1, 0.9]), 7.1)

    def test_negative_positive_float(self):
        self.assertEqual(max_integer([-5, 6, -10, -11.9, 9.2]), 9.2)

    def test_list_string(self):
        self.assertEqual(max_integer(["6", "45", "33", "9.2"]), "9.2")

    def test_None_element(self):
        with self.assertRaises(TypeError):
            max_integer(["6", "45", None, "9.2"])

    def test_not_list_int(self):
        with self.assertRaises(TypeError):
            max_integer(9.2)

    def test_notList(self):
        with self.assertRaises(TypeError):
            max_integer(33)

    def test_not_list_string(self):
        self.assertEqual(max_integer(["toto"]), "toto")

    def test_not_list_dict(self):
        with self.assertRaises(KeyError):
            max_integer({"toto": 3, "jsp": 4, "GG": 999, "legume": 0})


if __name__ == '__main__':
    unittest.main()
