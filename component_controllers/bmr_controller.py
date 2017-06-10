from calculation.user import User
from component_controllers.base_component_controller import BaseComponentController


class BMRController(BaseComponentController):
    _required_input = ['sex', 'age', 'weight', 'height']

    def control(self):
        """
        Call the BMR-calculator and output result.
        """
        bmr_input = self._get_required_input_from_user()
        bmr_input['bmr'] = User(self._serializer, **bmr_input).calculate_bmr()
        self._serializer.add_bmr(**bmr_input)
        self._view.bmr_data_output(**bmr_input)