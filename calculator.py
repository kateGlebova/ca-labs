EXERCISE_LEVELS = {
    'None': 1,
    'Sedentary': 1.2,
    'Light': 1.375,
    'Moderate': 1.55,
    'Hard': 1.725,
    'Non-Stop': 1.9
}


def male_bmr(weight, height, age):
    """
    Calculate and return a man's basal metabolic rate
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :return: float or int | BMR or -1 if parameters are not valid
    """
    if weight <= 0 or height <= 0 or age <= 0:
        return -1
    return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)


def female_bmr(weight, height, age):
    """
    Calculate and return a woman's basal metabolic rate
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :return: float or int | BMR or -1 if parameters are not valid
    """
    if weight <= 0 or height <= 0 or age <= 0:
        return -1
    return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)


def bmr_calculator(sex, weight, height, age):
    """
    Calculate a person's basal metabolic rate
    :param sex: string | 'male' or 'female'
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :return: float or int | BMR or -1 if parameters are not valid
    """
    BMR = {'male': male_bmr, 'female': female_bmr}
    if sex not in ('male', 'female'):
        return -1
    return BMR[sex](weight, height, age)


def calories_calculator(sex, weight, height, age, exercise_level):
    """
    Calculate daily calorie needs for person with specified parameters.
    :param sex: string | 'male' or 'female'
    :param weight: float | weight in kilograms
    :param height: float | height in centimeters
    :param age: int | age in years
    :param exercise_level: string | name of the exercise level
    :return: float or int | person's daily calories or -1 if parameters are not valid
    """
    bmr = bmr_calculator(sex, weight, height, age)
    if bmr == -1:
        return -1
    return EXERCISE_LEVELS[exercise_level] * bmr
