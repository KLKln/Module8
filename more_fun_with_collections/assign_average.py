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
    letter_grade = ''
    #switch statments go here
    for i in list_of_scores:

        if int(i) >= 90:
            letter_grade =  'A'
        elif int(i) >= 80:
            letter_grade = 'B'
        elif int(i) >= 70:
            letter_grade = 'C'
        elif int(i) >= 60:
            letter_grade = 'D'
            #'B':90,
            #'C':80,
            #'D':70,
            #'F':60




        return letter_grade



def switch_average(list_of_grades):
    """
Use reST style.
:param list_of_grades:
:return: letter_grade
raises keyError: raises an exception
    """
    #return_score = 0
    #make similar function wise to a switch statement
    #using a dictionary and if, elif, else

    list_of_scores = [100, 95, 78, 85, 99, 98]
    #loop to get each value in a list_of_grades
    list_of_scores +=[get_switch_value(value)]
    #for each score in list , add to sum, divide by length
    #return average
    a_dict =  {
        'A':100,
        'B':90,
        'C':80,
        'D':70,
        'F':60
    }


pass
