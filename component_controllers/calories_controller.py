from component_controllers.base_component_controller import BaseComponentController
from user import User


class CaloriesController(BaseComponentController):
    _required_input = ['sex', 'age', 'weight', 'height', 'exercise_level']

    def control(self):
        """
        Call daily calories rate calculator and output result.
        """
        calories_input = self._get_required_input_from_user()
        calories_input['calories'] = User(self._serializer, **calories_input).calculate_bmr()
        self._serializer.add_calories(**calories_input)
        self._view.daily_data_output(**calories_input)

