from abc import ABCMeta


class Serializer:
    __metaclass__ = ABCMeta

    def __init__(self, path, mode='r'):
        self._path = path
        self._obj = self.load(mode)

    def load(self, mode):
        """
        Deserialize object from the file.
        :return: object
        """
        try:
            with open(self._path, mode) as f:
                return self.s_load(f)
        except FileNotFoundError:
            return {}

    def add_bmr(self, sex, age, weight, height, bmr):
        """
        Add BMR entry to the object.
        :param sex: string | 'male' or 'female'
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param age: int | age in years
        :param bmr: float | basal metabolic rate
        """
        if 'bmr' not in self._obj:
            self._obj['bmr'] = {}

        if bmr not in self._obj['bmr']:
            self._obj['bmr'][bmr] = {'sex': sex, 'age': age, 'weight': weight, 'height': height}

    def add_bmi(self, weight, height, bmi):
        """
        Add BMR entry to the object.
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param bmi: float | body mass index
        """
        if 'bmi' not in self._obj:
            self._obj['bmi'] = {}

        if bmi not in self._obj['bmi']:
            self._obj['bmi'][bmi] = {'weight': weight, 'height': height}

    def add_calories(self, sex, age, weight, height, exercise_level, calories):
        """
        Add daily rate entry to the object.
        :param sex: string | 'male' or 'female'
        :param weight: float | weight in kilograms
        :param height: float | height in centimeters
        :param age: int | age in years
        :param exercise_level: string | name of the exercise level
        :param calories: float | daily rate
        """
        if 'calories' not in self._obj:
            self._obj['calories'] = {}

        if calories not in self._obj['calories']:
            self._obj['calories'][calories] = {
                'sex': sex,
                'age': age,
                'weight': weight,
                'height': height,
                'exercise_level': exercise_level
            }

    def dump(self):
        """
        Serialize object to the file.
        """
        with open(self._path, 'w') as f:
            self.s_dump(f)

    def s_load(self, f):
        """
        Library loader function of the concrete format.
        :return: deserialized object
        """
        raise NotImplementedError()

    def s_dump(self, f):
        """
        Library dumper function of the concrete format.
        :return: None
        """
        raise NotImplementedError()
