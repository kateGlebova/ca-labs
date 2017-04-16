import view as v
import sys
import calculator as c


def get_sex():
    sex = v.sex_input()
    while sex is None:
        sex = v.sex_input()
    return sex


def get_age():
    age = v.age_input()
    while age is None:
        age = v.age_input()
    return age


def get_weight():
    weight = v.weight_input()
    while weight is None:
        weight = v.weight_input()
    return weight


def get_height():
    height = v.height_input()
    while height is None:
        height = v.height_input()
    return height


def bmr_control(sex, weight, height, age):
    bmr = c.bmr_calculator(sex, weight, height, age)
    v.bmr_data_output(sex, weight, height, age, bmr)


def daily_control(sex, weight, height, age):
    exercise_level = v.exercise_level_input()
    while exercise_level is None:
        exercise_level = v.exercise_level_input()
    daily_rate = c.calories_calculator(sex, weight, height, age, exercise_level)
    v.daily_data_output(sex, weight, height, age, exercise_level, daily_rate)


def bmi_control(weight, height):
    bmi = c.bmi_calculator(weight, height)
    v.bmi_data_output(weight, height, bmi)


def full_control(sex, weight, height, age):
    exercise_level = v.exercise_level_input()
    while exercise_level is None:
        exercise_level = v.exercise_level_input()
    daily_rate = c.calories_calculator(sex, weight, height, age, exercise_level)
    bmi = c.bmi_calculator(weight, height)
    bmr = c.bmr_calculator(sex, weight, height, age)
    v.full_output(sex, weight, height, age, exercise_level, daily_rate, bmr, bmi)


def choice_analysis(choice, sex, weight, height, age):
    if choice == 1:
        bmr_control(sex, weight, height, age)
    elif choice == 2:
        daily_control(sex, weight, height, age)
    elif choice == 3:
        bmi_control(weight, height)
    elif choice == 4:
        full_control(sex, weight, height, age)


def main():
    choice = v.menu()
    while choice != 5:
        while choice is None:
            choice = v.menu()

        sex = get_sex()
        age = get_age()
        weight = get_weight()
        height = get_height()

        choice_analysis(choice, sex, weight, height, age)
        choice = v.menu()

    sys.exit(0)

if __name__ == '__main__':
    main()
