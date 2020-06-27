"""
Program: dict_membership.py
Author:  Kelly Klein
Date: 06/27/2020

This program accept a dictionary and key and return a boolean value stating
if the key is in the dictionary.
"""
def in_dict(a_dict, key):
    """
    use reST style
    :param a_dict:
    :param key:
    :returns: a boolean based on if key is in the dictionary
    :raises keyError:
    """

    i_d = True
    for x in a_dict:
        if key not in a_dict:
            i_d = False
            break
    return i_d


if __name__ == '__main__':
    pass
pass
