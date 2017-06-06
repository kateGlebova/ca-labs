from component_controllers.base_component_controller import BaseComponentController
from user import User


class AllComponentsController(BaseComponentController):
    _required_input = ['sex', 'age', 'weight', 'height', 'exercise_level']

    def control(self):
        """
        Call all of the calculators and output results.
        """
        all_input = self._get_required_input_from_user()
        user = User(self._serializer, **all_input)

        bmr = user.calculate_bmr()
        self._serializer.add_bmr(all_input['sex'], all_input['age'], all_input['weight'], all_input['height'], bmr)

        bmi = user.calculate_bmi()
        self._serializer.add_bmi(all_input['weight'], all_input['height'], bmi)

        calories = user.calculate_calories()

        self._view.full_output(**all_input, bmr=bmr, bmi=bmi, calories=calories)
