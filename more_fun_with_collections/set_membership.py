"""
Program: set_membership.py
Author:  Kelly Klein
Date: 06/27/2020

This program accept a set and element and return a boolean value stating
if the element is in the set.
"""


def in_set(a_set, element):
    """
    use reST style
    :param a_set:
    :param element:
    :returns: a boolean based on if element is in the set
    :raises keyError:
    """
    i_s = True
    for x in a_set:
        if element not in a_set:
            i_s = False
            break
    return i_s



if __name__ == '__main__':
    pass

