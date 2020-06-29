import unittest
from more_fun_with_collections import assign_average as aa


class MyTestCase(unittest.TestCase):

    def test_a(self):
        self.assertEqual(aa.get_switch_value({95,95,95}), 'A')

    def test_b(self):
        self.assertEqual(aa.get_switch_value({85,85,85}), 'B')

    def test_c(self):
        self.assertEqual(aa.get_switch_value({75,75,75}), 'C')

    def test_d(self):
        self.assertEqual(aa.get_switch_value({65,65,65}), 'D')

    def test_f(self):
        self.assertEqual(aa.get_switch_value({55,55,55}), 'F')

    def test_non_key(self):
        self.assertEqual(aa.get_switch_value({101, -5, 155}), 'Not a viable score!')


if __name__ == '__main__':
    unittest.main()
