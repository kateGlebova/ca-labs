EXERCISE_LEVELS = {
    'None': 1,
    'Sedentary': 1.2,
    'Light': 1.375,
    'Moderate': 1.55,
    'Hard': 1.725,
    'Non-Stop': 1.9
}
DIET_MODES = {
    'Safe': 0.85,
    'Quick': 0.75,
    'Extra': 0.6
}


def calories_calculator(sex, weight, height, age, exercise_level):
    """
    Calculate daily calorie needs for person with specified parameters and return
    either person's daily calories or -1 if parameters are not valid.
    :param sex: string | 'male' or 'female'
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :param exercise_level: string | name of the exercise level
    :return:
    """
    if not (sex in ('male', 'female') and exercise_level in EXERCISE_LEVELS and weight > 0 and height > 0):
        return -1

    if sex == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return EXERCISE_LEVELS[exercise_level] * bmr


def losing_weight(sex, weight, height, age, exercise_level, mode):
    """
    Calculate daily calorie needs for person who wants to lose weight with specified parameters and return
    either person's daily calories or -1 if parameters are not valid.
    :param sex: string | 'male' or 'female'
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :param exercise_level: string | name of the exercise level
    :param mode: string | name of the diet mode
    :return:
    """
    if not (mode in DIET_MODES):
        return -1

    return DIET_MODES[mode] * calories_calculator(sex, weight, height, age, exercise_level)
