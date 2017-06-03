"""
Controller module.
"""

import sys
from configparser import ConfigParser

from os.path import join, dirname

import calculator as c
from calculator import EXERCISE_LEVELS

import view as v
from serialization.json_serialization import JSONSerializer
from serialization.pickle_serialization import PICKLESerializer
from serialization.yaml_serialization import YAMLSerializer


def get_format():
    config = ConfigParser()
    config.read(join(dirname(__file__), 'conf.ini'))
    return config['serialization']['serialization_format']


def load_serializer():
    formats = {'json': JSONSerializer, 'yaml': YAMLSerializer, 'pickle': PICKLESerializer}
    format = get_format()
    try:
        return formats[format]()
    except KeyError:
        print('%s serialization format is not supported.' % format)
        sys.exit(1)


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


def bmr_control(srlzr, sex, weight, height, age):
    """
    Call the BMR-calculator and output result.
    :param srlzr: Serializer subclass | serializer
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    bmr = c.bmr_calculator(sex, weight, height, age)
    srlzr.add_bmr(sex, age, weight, height, bmr)
    v.bmr_data_output(sex, weight, height, age, bmr)


def daily_control(srlzr, sex, weight, height, age):
    """
    Call daily calorie calculator and output result.
    :param srlzr: Serializer subclass | serializer
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    exercise_level = get_exercise_level()
    daily_rate = c.calories_calculator(sex, weight, height, age, exercise_level)
    srlzr.add_calories(sex, age, weight, height, exercise_level, daily_rate)
    v.daily_data_output(sex, weight, height, age, exercise_level, daily_rate)


def bmi_control(srlzr, weight, height):
    """
    Call the BMI-calculator and output result.
    :param srlzr: Serializer subclass | serializer
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    bmi = c.bmi_calculator(weight, height)
    srlzr.add_bmi(weight, height, bmi)
    v.bmi_data_output(weight, height, bmi)


def full_control(srlzr, sex, weight, height, age):
    """
    Call all of the calculators and output results.
    :param srlzr: Serializer subclass | serializer
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

    srlzr.add_bmr(sex, age, weight, height, bmr)
    srlzr.add_calories(sex, age, weight, height, exercise_level, daily_rate)
    srlzr.add_bmi(weight, height, bmi)

    v.full_output(sex, weight, height, age, exercise_level, daily_rate, bmr, bmi)


def choice_analysis(srlzr, choice, sex, weight, height, age):
    """
    Call a necessary calculators depending on a user's choice.
    :param srlzr: Serializer subclass | serializer
    :param choice: int | choice code
    :param sex: string | 'male' or 'female'
    :param age: int | age in years
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :return: None
    """
    if choice == 1:
        bmr_control(srlzr, sex, weight, height, age)
    elif choice == 2:
        daily_control(srlzr, sex, weight, height, age)
    elif choice == 3:
        bmi_control(srlzr, weight, height)
    elif choice == 4:
        full_control(srlzr, sex, weight, height, age)


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
    srlzr = load_serializer()
    choice = make_choice()
    while choice != 5:
        sex = get_sex()
        age = get_age()
        weight = get_weight()
        height = get_height()
        choice_analysis(srlzr, choice, sex, weight, height, age)
        choice = make_choice()

    srlzr.dump()
    sys.exit(0)


if __name__ == '__main__':
    main()
