"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
from more_fun_with_collections import set_membership as sm


class MyTestCase(unittest.TestCase):

    def test__in_set_true(self):
        #create a set as a variable
        a_set = [1, 3, 5, 7, 9]
        #create an element as a variable
        element = [3, 5]
        #assertTrue, expect  True to be the result
        #assertTrue(function_name(parameter11, parameter2)
        self.assertTrue(sm(a_set), element)

    def test__in_set_false(self):
        #create a set as a variable
        a_set = [1, 3, 5, 7, 9]
        #create an element as a variable
        element =[2, 4]
        #assertFalse, expect False to be the result
        #assertFalse(function_name(parameter11, parameter2)
        self.assertFalse(sm(a_set), element)


if __name__ == '__main__':
    unittest.main()
