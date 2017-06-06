from calculator import Calculator


class BaseComponentController:
    def __init__(self, srlzr, view):
        self._view = view
        self._serializer = srlzr

        self._input_functions = {
            'sex': self._input_sex,
            'age': self._input_age,
            'weight': self._input_weight,
            'height': self._input_height,
            'exercise_level': self._input_exercise_level
        }

    def control(self):
        raise NotImplementedError()

    @property
    def _required_input(self):
        return self._required_input

    def _get_required_input_from_user(self):
        input_dict = {inp: self._input_functions[inp]() for inp in self._required_input}
        return input_dict

    @staticmethod
    def _controller_input(view_input, *k):
        data = view_input(*k)
        while data is None:
            data = view_input(*k)
        return data

    def _input_sex(self):
        """
        Ask for the user's sex and get his/her answer while he/she doesn't enter a valid value.
        :return: string | 'male' or 'female'
        """
        return self._controller_input(self._view.sex_input)

    def _input_age(self):
        """
        Ask for the user's age and get his/her answer while he/she doesn't enter a valid value.
        :return: int | age in years
        """
        return self._controller_input(self._view.age_input)

    def _input_weight(self):
        """
        Ask for the user's weight and get his/her answer while he/she doesn't enter a valid value.
        :return: float | weight in kilograms
        """
        return self._controller_input(self._view.weight_input)

    def _input_height(self):
        """
        Ask for the user's height and get his/her answer while he/she doesn't enter a valid value.
        :return: float | height in centimeters
        """
        return self._controller_input(self._view.height_input)

    def _input_exercise_level(self):
        """
        Ask for the user's exercise level and get his/her answer while he/she doesn't enter a valid value.
        :return: string | exercise level
        """
        choices = list(Calculator.exercise_levels)
        return self._controller_input(self._view.exercise_level_input, choices)
