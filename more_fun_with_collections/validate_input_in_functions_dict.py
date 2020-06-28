"""
Program: validate_input_in_functions_dict.py
Author: Kelly Klein
Last date modified: 6/17/2020
This program will .
"""


def get_test_scores():
    """
Use reST style.
:param invalid_message:"invalid test score, try again!"
:return: test_name, test_score
raises keyError: raises an exception
    """

    scores_dict = dict()
    num_scores = input('How many test scores do you have?')
    # loop to get num_scores input
    while True:
        try:
            x = 1
            while x <= int(num_scores):
                score = input('Please enter test score: ')
                if score.isalpha():
                    raise TypeError
                if 0 <= int(score) <= 100:
                    dictionary_update = {'test' + str(x): int(score)}
                    if str(x) not in scores_dict.keys():
                        scores_dict.update(dictionary_update)
                    x += 1
                else: raise TypeError
        except TypeError:
            print("positive numbers only please")
            continue

    # return scores_dict
        for key, value in scores_dict.items():
            return print(key,':',value)



# Key valuepair, score is going to be the value
# I define the key
def average_scores(scores_dict):
    # num_scores = get length of dictionary
    num_scores = len(scores_dict)
    # parse every score in dictionary
    value = 0
    for x in scores_dict.values():
        value += x
        # calculate the average
        average = value / num_scores
        return average


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
Use reST style.
:param test_name: input for name of test
:param test_score: score the student got on test
:param invalid_message:"invalid test score, try again!"
:return: test_name, test_score
raises keyError: raises an exception
    """
    while True:

        try:
            print("test_name is:", test_name)
            print("test_score is: ", test_score)
            print("invalid_message is:", invalid_message)
        except ValueError:
            raise ValueError(invalid_message)
        if int(test_score) < 0:
            return False
        elif int(test_score) > 100:
            return False
        else:
            test = (test_name + ':' + " " + str(test_score))

        # return { test_name: test_score}
        return test


if __name__ == '__main__':
    get_test_scores()
