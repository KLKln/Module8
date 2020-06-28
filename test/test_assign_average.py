import unittest
import unittest.mock as mock
from more_fun_with_collections import assign_average as aa


class MyTestCase(unittest.TestCase):

    def test_one_hundred(self):
        self.assertEqual(aa.get_switch_value({100, 100, 100}), 'A')

    def test_ninety(self):
        self.assertEqual(aa.get_switch_value({90, 90, 90}), 'B')

    def test_eighty(self):
        self.assertEqual(aa.get_switch_value({80, 80, 80}), 'C')

    def test_seventy(self):
        self.assertEqual(aa.get_switch_value({70, 70, 70}), 'D')

    def test_sixty(self):
        self.assertEqual(aa.get_switch_value({60, 60, 60}), 'F')

    def test_non_key(self):
        self.assertRaises(aa.get_switch_value('A'), 'raises error')


if __name__ == '__main__':
    unittest.main()
