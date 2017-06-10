"""
Calories calculator module.
"""


class Calculator:
    exercise_levels = {
        'None': 1,
        'Sedentary': 1.2,
        'Light': 1.375,
        'Moderate': 1.55,
        'Hard': 1.725,
        'Non-Stop': 1.9
    }

    @staticmethod
    def _male_bmr(weight, height, age):
        """
        Calculate and return a man's basal metabolic rate
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param age: int | age in years
        :return: float or int | BMR or -1 if parameters are not valid
        """
        if weight < 0 or height < 0 or age < 0:
            raise ValueError('Weight, height and age cannot be negative.')
        return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

    @staticmethod
    def _female_bmr(weight, height, age):
        """
        Calculate and return a woman's basal metabolic rate
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param age: int | age in years
        :return: float or int | BMR or -1 if parameters are not valid
        """
        if weight < 0 or height < 0 or age < 0:
            raise ValueError('Weight, height and age cannot be negative.')
        return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    def bmr_calculator(self, sex, weight, height, age):
        """
        Calculate a person's basal metabolic rate
        :param sex: string | 'male' or 'female'
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param age: int | age in years
        :return: float or int | BMR or -1 if parameters are not valid
        """
        BMR = {'male': self._male_bmr, 'female': self._female_bmr}
        if sex not in ('male', 'female'):
            raise ValueError("Sex can only be male or female.")
        return BMR[sex](weight, height, age)

    def calories_calculator(self, sex, weight, height, age, exercise_level):
        """
        Calculate daily calorie needs for person with specified parameters.
        :param sex: string | 'male' or 'female'
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param age: int | age in years
        :param exercise_level: string | name of the exercise level
        :return: float or int | person's daily calories or -1 if parameters are not valid
        """
        bmr = self.bmr_calculator(sex, weight, height, age)
        if exercise_level not in self.exercise_levels:
            raise ValueError('Exercise level can only be %s.' % '/'.join(self.exercise_levels.keys()))
        return self.exercise_levels[exercise_level] * bmr

    @staticmethod
    def bmi_calculator(weight, height):
        """
        Calculate a person's body mass index.
        :param weight: float | weight in kilograms
        :param height: height in centimeters
        :return: float or int | person's body mass index or -1 if parameters are not valid
        """
        if weight < 0 or height < 0:
            raise ValueError('Weight and height cannot be negative.')
        height_meters = height / 100
        bmi = weight / height_meters ** 2
        return bmi
