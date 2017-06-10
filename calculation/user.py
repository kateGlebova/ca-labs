"""
User class.

Holds information about one user with weight and height as minimum data, calculates and serializes BMR,
daily calories rate and BMI.
"""
from calculation.calculator import Calculator


class User:
    def __init__(self, serializer, height=None, weight=None, sex=None, age=None, exercise_level=None):
        self._sex = sex
        self._age = age
        self._height = height
        self._weight = weight
        self._exercise_level = exercise_level
        self._calculator = Calculator()
        self._serializer = serializer


    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value and value not in ('male', 'female'):
            raise ValueError('Sex can only be male or female.')

        self._sex = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value and value < 0:
            raise ValueError('Age cannot be negative.')

        self._age = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not value:
            raise ValueError('Height is necessary for all computations.')
        if value < 0:
            raise ValueError('Height cannot be negative.')

        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if not value:
            raise ValueError('Weight is necessary for all computations.')
        if value < 0:
            raise ValueError('Weight cannot be negative.')

        self._weight = value

    @property
    def exercise_level(self):
        return self._exercise_level

    @exercise_level.setter
    def exercise_level(self, value):
        if value and value not in self._calculator.exercise_levels:
            raise ValueError('Exercise level can only be %s.' %  '/'.join(self._calculator.exercise_levels.keys()))

        self._age = value

    def calculate_bmr(self):
        if not (self.sex and self.age):
            raise ValueError('Sex and age must be specified to calculate BMR.')

        bmr = self._calculator.bmr_calculator(self.sex, self.weight, self.height, self.age)
        self._serializer.add_bmr(self.sex, self.age, self.weight, self.height, bmr)
        return bmr

    def calculate_calories(self):
        if not (self.sex and self.age and self.exercise_level):
            raise ValueError('Sex, age, and exercise level must be specified to calculate daily calories rate.')

        calories = self._calculator.calories_calculator(self.sex, self.weight, self.height, self.age, self.exercise_level)
        self._serializer.add_calories(self.sex, self.age, self.weight, self.height, self.exercise_level, calories)
        return calories

    def calculate_bmi(self):
        bmi = self._calculator.bmi_calculator(self.weight, self.height)
        self._serializer.add_bmi(self.weight, self.height, bmi)
        return bmi