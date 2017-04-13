EXERCISE_LEVELS = {
    'None': 1,
    'Sedentariness': 1.2,
    'Light': 1.375,
    'Moderate': 1.55,
    'Hard': 1.725,
    'Non-Stop': 1.9
}


def calories_calculator(sex, weight, height, age, exersice_level):
    """
    Calculate daily calorie needs for person with specified paranmeters and return
    either person's daily calories or -1 if parameters are not valid.
    :param sex: string | 'male' or 'female'
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :param exersice_level: int | code of the exercise level
    :return:
    """
    if not (sex in ('male', 'female') and exersice_level in EXERCISE_LEVELS and weight > 0 and height > 0):
        return -1

    if sex == 'male':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return EXERCISE_LEVELS[exersice_level] * BMR
