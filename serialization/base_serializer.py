class Serializer:
    """
    An abstract calculator serializer.

    Methods s_load, s_dump must be implemented in the derived classes.
    """

    def __init__(self, path):
        """
        Initialise _path attribute and load object (_obj) from the file specified in _path.
        :param path: string | path to the file with the object
        """
        self._path = path
        self._obj = self._load()

    @property
    def _mode(self):
        """
        Reading/writing mode attribute ('b' or '').
        """
        raise NotImplementedError()

    def _load(self):
        """
        Deserialize object from the file.
        :return: object
        """
        try:
            with open(self._path, 'r' + self._mode) as f:
                return self.s_load(f)
        except (FileNotFoundError, ValueError):
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
        with open(self._path, 'w' + self._mode) as f:
            self.s_dump(self._obj, f)

    @staticmethod
    def s_load(f):
        """
        Library loader function of the concrete format.
        :return: deserialized object
        """
        raise NotImplementedError()

    @staticmethod
    def s_dump(obj, f):
        """
        Library dumper function of the concrete format.
        :return: None
        """
        raise NotImplementedError()