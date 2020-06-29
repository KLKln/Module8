"""
Program: assign_average.py
Author: Kelly Klein
Last date modified: 6/28/2020
This program will take in a list of scores and return an average and letter grade.
"""


def get_switch_value(list_of_scores):
    """
Use reST style.
:param list_of_scores:
:return: letter_grade
raises keyError: raises an exception
    """
    for i in list_of_scores:
        if int(i) >= 90:
            letter_grade = 'A'
        elif int(i) >= 80:
            letter_grade = 'B'
        elif int(i) >= 70:
            letter_grade = 'C'
        elif int(i) >= 60:
            letter_grade = 'D'
        elif 0 <= int(i) <= 59:
            letter_grade = 'F'
        else:
            letter_grade = 'Not a viable score!'

        return letter_grade


def switch_average(list_of_scores):
    """
Use reST style.
:param list_of_scores:
:return: average
raises keyError: raises an exception
    """
    average = sum(list_of_scores)/len(list_of_scores)
    if average >= 90:
        average_grade = 'A'
    elif average >= 80:
        average_grade = 'B'
    elif average >= 70:
        average_grade = 'C'
    elif average >= 60:
        average_grade = 'D'
    elif 0 <= average <= 59:
        average_grade = 'F'
    else:
        average_grade = 'Not a viable score!'
    return print('your average score is:', average, ', which makes your average grade:', average_grade)


if __name__ == '__main__':
    switch_average(list_of_scores = [100, 95, 78, 85, 99, 98])

