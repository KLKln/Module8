import unittest
from datetime import datetime
from half_birthday import half_birth as hb


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        most_recent_birthday = datetime(2020, 3, 21)
        expected_date = datetime(2020, 9, 19)
        self.assertEqual(expected_date, hb.get_half_birthday(most_recent_birthday))


if __name__ == '__main__':
    unittest.main()
