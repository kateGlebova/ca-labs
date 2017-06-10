from calculation.calculator import Calculator


class BaseComponentController:
    """
    An abstract controller that particular calculation controllers derive from.
    """
    def __init__(self, srlzr, view):
        """
        Initialise _serializer, _view objects and dictionary with corresponding input functions.
        :param srlzr: Serializer subclass
        :param view: View
        """
        self._view = view
        self._serializer = srlzr

        self._input_functions = {
            'sex': self._input_sex,
            'age': self._input_age,
            'weight': self._input_weight,
            'height': self._input_height,
            'exercise_level': self._input_exercise_level
        }

    @property
    def _required_input(self):
        return self._required_input

    def control(self):
        """
        An abstract method that should be implemented in all derived classes.
        """
        raise NotImplementedError()

    def _get_required_input_from_user(self):
        """
        Ask user for the required for the particular computation input.
        :return: dict | input
        """
        input_dict = {inp: self._input_functions[inp]() for inp in self._required_input}
        return input_dict

    @staticmethod
    def _controller_input(view_input, *k):
        """
        Ask user for input, repeat if nothing was entered.
        :param view_input: func | view input function
        :param k: arbitary positional arguments for the view function
        :return: str | input data
        """
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
