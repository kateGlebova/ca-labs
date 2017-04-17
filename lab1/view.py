from terminaltables import AsciiTable


def validation(is_valid, inp, error_message='Invalid input.'):
    if is_valid:
        return inp
    print(error_message, '\n')


def menu():
    print('\n[1] BMR Calculator(Basal Metabolic Rate Calculator)')
    print('[2] Daily Calorie Calculator')
    print('[3] BMI Calculator(Body Mass Index Calculator)')
    print('[4] View all')
    print('[5] Quit')
    try:
        choice = int(input('Your choice: '))
    except ValueError:
        return validation(False, None)
    return validation(1 <= choice <= 6, choice)


def sex_input():
    sex = input('Enter your sex ("male" / "female"): ')
    return validation(sex in ('male', 'female'), sex)


def age_input():
    try:
        age = int(input('Enter your age (in years): '))
    except ValueError:
        return validation(False, None)
    return validation(age > 0, age)


def weight_input():
    try:
        weight = float(input('Enter your weight(in kilograms): '))
    except ValueError:
        return validation(False, None)
    return validation(weight > 0, weight)


def height_input():
    try:
        height = float(input('Enter your height(in centimeters): '))
    except ValueError:
        return validation(False, None)
    return validation(height > 0, height)


def exercise_level_input(choices):
    exercise_level = input('Enter exercise level (%s): ' % '/'.join(choices))
    return validation(exercise_level in choices, exercise_level)


def data_output(header, row, caption):
    row = [isinstance(element, float) and "%.2f" % element or element for element in row]
    print('\n', AsciiTable([header, row], caption).table)


def physique_data_output(sex, age, weight, height):
    data_output(['SEX', 'AGE', 'WEIGHT', 'HEIGHT'], [sex, age, weight, height], 'PHYSIQUE')


def bmi_data_output(weight, height, bmi):
    data_output(['WEIGHT', 'HEIGHT', 'BMI'], [weight, height, bmi], 'Body Mass Index Calculator')


def daily_data_output(sex, age, weight, height, exercise_level, daily_rate):
    data_output(
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'EXERCISE LEVEL', 'DAILY RATE'],
        [sex, age, weight, height, exercise_level, daily_rate],
        'Daily Calorie Calculator'
    )


def bmr_data_output(sex, weight, height, age, bmr):
    data_output(
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'BMR'],
        [sex, age, weight, height, bmr],
        'Basal Metabolic Rate Calculator'
    )


def full_output(sex, weight, height, age, exercise_level, daily_rate, bmr, bmi):
    data_output(
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'EXERCISE LEVEL', 'DAILY RATE', 'BMR', 'BMI'],
        [sex, age, weight, height, exercise_level, daily_rate, bmr, bmi],
        'Full Calculations'
    )
