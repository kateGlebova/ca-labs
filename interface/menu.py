import sys

from component_controllers.all_components_controller import AllComponentsController
from component_controllers.bmi_controller import BMIController
from component_controllers.bmr_controller import BMRController
from component_controllers.calories_controller import CaloriesController
from interface.interface import Interface


class Menu(Interface):
    def launch(self):
        choice = self._make_choice()
        while choice != 5:
            self._choice_analysis(choice)
            choice = self._make_choice()

        self._serializer.dump()
        sys.exit(0)

    def _choice_analysis(self, choice):
        """
        Instantiate necessary controller depending on a user's choice and call its control method.
        :param choice: int | choice code
        :return: None
        """
        if choice == 1:
            BMRController(self._serializer, self._view).control()
        elif choice == 2:
            CaloriesController(self._serializer, self._view).control()
        elif choice == 3:
            BMIController(self._serializer, self._view).control()
        elif choice == 4:
            AllComponentsController(self._serializer, self._view).control()

    def _make_choice(self):
        """
        Ask user to choose an option while he/she doesn't enter a valid value.
        :return: code of the piece of functionality or None
        """
        choice = self._view.menu()
        while choice is None:
            choice = self._view.menu()
        return choice
