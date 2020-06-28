import unittest
import unittest.mock as mock
from more_fun_with_collections import assign_average as aa


class MyTestCase(unittest.TestCase):

    def test_one_hundred(self):
        self.assertEqual(aa.get_switch_value({100, 100, 100}), {'A':100})

    def test_ninety(self):
        self.assertEqual(aa.get_switch_value({90, 90, 90}), {'B':90})

    def test_eighty(self):
        self.assertEqual(aa.get_switch_value({80, 80, 80}), {'C':80})

    def test_seventy(self):
        self.assertEqual(aa.get_switch_value({70, 70, 70}), {'D':70})

    def test_sixty(self):
        self.assertEqual(aa.get_switch_value(60), {'F':60})

    def test_non_key(self):
        self.assertRaises(aa.get_switch_value('A'), 'raises error')


if __name__ == '__main__':
    unittest.main()
