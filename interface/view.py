"""
Views class.
"""
from terminaltables import AsciiTable


class View:
    @staticmethod
    def _validation(is_valid, inp, error_message='Invalid input.'):
        """
        Print error message if the input is not valid.
        :param is_valid: bool | True if the input is valid, False otherwise
        :param inp: input
        :param error_message: string | error message
        :return: inp if the input is valid, None otherwise
        """
        if is_valid:
            return inp
        print(error_message, '\n')

    def menu(self):
        """
        Output the main menu and get user's choice.
        :return: code of the piece of functionality or None
        """
        print('\n[1] BMR Calculator(Basal Metabolic Rate Calculator)')
        print('[2] Daily Calorie Calculator')
        print('[3] BMI Calculator(Body Mass Index Calculator)')
        print('[4] View all')
        print('[5] Quit')
        try:
            choice = int(input('Your choice: '))
        except ValueError:
            return self._validation(False, None)
        return self._validation(1 <= choice <= 6, choice)

    def sex_input(self):
        """
        Ask for the user's sex and get his/her answer.
        :return: string | user's sex or None
        """
        sex = input('Enter your sex ("male" / "female"): ')
        return self._validation(sex in ('male', 'female'), sex)

    def age_input(self):
        """
        Ask for the user's age and get his/her answer.
        :return: int | user's age or None
        """
        try:
            age = int(input('Enter your age (in years): '))
        except ValueError:
            return self._validation(False, None)
        return self._validation(age > 0, age)

    def weight_input(self):
        """
        Ask for the user's weight and get his/her answer.
        :return: float | user's weight or None
        """
        try:
            weight = float(input('Enter your weight(in kilograms): '))
        except ValueError:
            return self._validation(False, None)
        return self._validation(weight > 0, weight)

    def height_input(self):
        """
        Ask for the user's height and get his/her answer.
        :return: float | user's height or None
        """
        try:
            height = float(input('Enter your height(in centimeters): '))
        except ValueError:
            return self._validation(False, None)
        return self._validation(height > 0, height)

    def exercise_level_input(self, choices):
        """
        Ask for the user's exercise level and get his/her answer.
        :param choices: list of strings | exercise levels a user can choose from
        :return: string | user's exercise level or None
        """
        exercise_level = input('Enter exercise level (%s): ' % '/'.join(choices))
        return self._validation(exercise_level in choices, exercise_level)

    @staticmethod
    def _data_output(header, row, caption):
        """
        Format all floats in a row and output the table.
        :param header: list of strings | header row cells
        :param row: list | info row cells
        :param caption: string | title of the table
        :return: None
        """
        row = [isinstance(element, float) and "%.2f" % element or element for element in row]
        print('\n', AsciiTable([header, row], caption).table)

    def bmi_data_output(self, weight, height, bmi):
        """
        Output user's BMI.
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param bmi: float | BMI
        :return: None
        """
        self._data_output(['WEIGHT', 'HEIGHT', 'BMI'], [weight, height, bmi], 'Body Mass Index Calculator')

    def daily_data_output(self, sex, age, weight, height, exercise_level, calories):
        """
        Output user's daily calorie needs.
        :param sex: string | 'male' or 'female'
        :param age: int | age in years
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param exercise_level: string | exercise level
        :param daily_rate: float | daily calories needs
        :return: None
        """
        self._data_output(
            ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'EXERCISE LEVEL', 'DAILY RATE'],
            [sex, age, weight, height, exercise_level, calories],
            'Daily Calorie Calculator'
        )

    def bmr_data_output(self, sex, weight, height, age, bmr):
        """
        Output user's BMR.
        :param sex: string | 'male' or 'female'
        :param age: int | age in years
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param bmr: float | BMR
        :return: None
        """
        self._data_output(
            ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'BMR'],
            [sex, age, weight, height, bmr],
            'Basal Metabolic Rate Calculator'
        )

    def full_output(self, sex, weight, height, age, exercise_level, calories, bmr, bmi):
        """
        Output user's daily calories needs, BMR, and BMI.
        :param sex: string | 'male' or 'female'
        :param age: int | age in years
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param exercise_level: string | exercise level
        :param daily_rate: float | daily calories needs
        :param bmr: float | BMR
        :param bmi: float | BMI
        :return: None
        """
        self._data_output(
            ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'EXERCISE LEVEL', 'DAILY RATE', 'BMR', 'BMI'],
            [sex, age, weight, height, exercise_level, calories, bmr, bmi],
            'Full Calculations'
        )
