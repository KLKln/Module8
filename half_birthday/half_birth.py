from datetime import datetime, timedelta
"""
Program: half_birth.py
Author: Kelly Klein
Last date modified: 6/28/2020
This program will take a users most recent birthday and return
their next half birthday.
"""


def get_half_birthday(most_recent_birthday):
    """
Use reST style.
:param most_recent_birthday
:return: half_birthday_date
    """
    half_birthday_date = most_recent_birthday + timedelta(days=182)

    return half_birthday_date
