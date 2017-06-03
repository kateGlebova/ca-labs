from abc import ABCMeta


class Serializer:
    __metaclass__ = ABCMeta

    def __init__(self, path):
        self._path = path
        self.obj = self.load()

    def load(self):
        """
        Deserialize object from the file.
        :return: object
        """
        try:
            with open(self._path) as f:
                return self.s_load(f)
        except FileNotFoundError:
            return {}

    def add_bmr(self, sex, age, weight, height, bmr):
        if 'bmr' not in self.obj:
            self.obj['bmr'] = {}

        if bmr not in self.obj['bmr']:
            self.obj['bmr'][bmr] = {'sex': sex, 'age': age, 'weight': weight, 'height': height}

    def add_bmi(self, weight, height, bmi):
        if 'bmi' not in self.obj:
            self.obj['bmi'] = {}

        if bmi not in self.obj['bmi']:
            self.obj['bmi'][bmi] = {'weight': weight, 'height': height}

    def add_calories(self, sex, age, weight, height, exercise_level, calories):
        if 'calories' not in self.obj:
            self.obj['calories'] = {}

        if calories not in self.obj['calories']:
            self.obj['calories'][calories] = {
                'sex': sex,
                'age': age,
                'weight': weight,
                'height': height,
                'exercise_level': exercise_level
            }

    def dump(self):
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
