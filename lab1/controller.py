"""
Controller module.
"""

import lab1.view as v
import sys
import lab1.calculator as c

from lab1.calculator import EXERCISE_LEVELS


def get_sex():
    """
    Ask for the user's sex and get his/her answer while he/she doesn't enter a valid value.
    :return: string | 'male' or 'female'
    """
    sex = v.sex_input()
    while sex is None:
        sex = v.sex_input()
    return sex


def get_age():
    """
    Ask for the user's age and get his/her answer while he/she doesn't enter a valid value.
    :return: int | age in years
    """
    age = v.age_input()
    while age is None:
        age = v.age_input()
    return age


def get_weight():
    """
    Ask for the user's weight and get his/her answer while he/she doesn't enter a valid value.
    :return: float | weight in kilograms
    """
    weight = v.weight_input()
    while weight is None:
        weight = v.weight_input()
    return weight


def get_height():
    """
    Ask for the user's height and get his/her answer while he/she doesn't enter a valid value.
    :return: float | height in centimeters
    """
    height = v.height_input()
    while height is None:
        height = v.height_input()
    return height


def get_exercise_level():
    """
    Ask for the user's exercise level and get his/her answer while he/she doesn't enter a valid value.
    :return: string | exercise level
    """
    choices = list(EXERCISE_LEVELS.keys())
    exercise_level = v.exercise_level_input(choices)
    while exercise_level is None:
        exercise_level = v.exercise_level_input(choices)
    return exercise_level


def bmr_control(sex, weight, height, age):
    """
    Call the BMR-calculator and output result.
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    bmr = c.bmr_calculator(sex, weight, height, age)
    v.bmr_data_output(sex, weight, height, age, bmr)


def daily_control(sex, weight, height, age):
    """
    Call daily calorie calculator and output result.
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    exercise_level = get_exercise_level()
    daily_rate = c.calories_calculator(sex, weight, height, age, exercise_level)
    v.daily_data_output(sex, weight, height, age, exercise_level, daily_rate)


def bmi_control(weight, height):
    """
    Call the BMI-calculator and output result.
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    bmi = c.bmi_calculator(weight, height)
    v.bmi_data_output(weight, height, bmi)


def full_control(sex, weight, height, age):
    """
    Call all of the calculators and output results.
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    exercise_level = get_exercise_level()
    daily_rate = c.calories_calculator(sex, weight, height, age, exercise_level)
    bmi = c.bmi_calculator(weight, height)
    bmr = c.bmr_calculator(sex, weight, height, age)
    v.full_output(sex, weight, height, age, exercise_level, daily_rate, bmr, bmi)


def choice_analysis(choice, sex, weight, height, age):
    """
    Call a necessary calculators depending on a user's choice.
    :param choice:
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    if choice == 1:
        bmr_control(sex, weight, height, age)
    elif choice == 2:
        daily_control(sex, weight, height, age)
    elif choice == 3:
        bmi_control(weight, height)
    elif choice == 4:
        full_control(sex, weight, height, age)


def make_choice():
    """
    Ask user to choose an option while he/she doesn't enter a valid value.
    :return: code of the piece of functionality or None
    """
    choice = v.menu()
    while choice is None:
        choice = v.menu()
    return choice


def main():
    """
    Control calculations depending on the user's choice
    :return: None
    """
    choice = make_choice()
    while choice != 5:
        sex = get_sex()
        age = get_age()
        weight = get_weight()
        height = get_height()
        choice_analysis(choice, sex, weight, height, age)
        choice = make_choice()
    sys.exit(0)

if __name__ == '__main__':
    main()
