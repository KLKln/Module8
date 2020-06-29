import unittest
import datetime
from half_birthday import half_birthday as hb

class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        most_recent_birthday = datetime.datetime(2020, 3, 21)
        #assertEquals (expectedAnaswer, function_call())
        expected_date = datetime.datetime(2020, 9, 21)
        self.assertEqual(expected_date(most_recent_birthday), hb.half_birthday(most_recent_birthday))


if __name__ == '__main__':
    unittest.main()
