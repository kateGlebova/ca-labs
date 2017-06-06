from component_controllers.base_component_controller import BaseComponentController
from user import User


class BMIController(BaseComponentController):
    _required_input = ['weight', 'height']

    def control(self):
        """
        Call the BMI-calculator and output result.
        """
        bmi_input = self._get_required_input_from_user()
        bmi_input['bmi'] = User(self._serializer, **bmi_input).calculate_bmi()
        self._serializer.add_bmi(**bmi_input)
        self._view.bmi_data_output(**bmi_input)
