"""
Program: set_membership.py
Author:  Kelly Klein
Date: 06/27/2020

This program accept a set and return a boolean value stating
if the element is in the set.
"""


def in_set(a_set, b_set):
    """
    use reST style
    :param a_set:
    :param element: element we are checking if in the set
    :returns: a boolean on if element is in the set
    :raises keyError:
    """
    i_s = True
    for x in a_set:
        if x in a_set:
            return True
        


