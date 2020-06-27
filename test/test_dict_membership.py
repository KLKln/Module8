import unittest
from more_fun_with_collections import dict_membership as dm


class MyTestCase(unittest.TestCase):

    def test_in_dict_true(self):
        #create a set as a variable
        a_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
        #create an element as a variable
        key = 'C'
        #assertTrue, expect  True to be the result
        #assertTrue(function_name(parameter11, parameter2)
        self.assertTrue(dm.in_dict(a_dict, key), key)

    def test_in_dict_false(self):
        #create a set as a variable
        a_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
        #create an element as a variable
        key = 'Z'
        #assertFalse, expect False to be the result
        #assertFalse(function_name(parameter11, parameter2)
        self.assertFalse(dm.in_dict(a_dict, key), key)


if __name__ == '__main__':
    unittest.main()
