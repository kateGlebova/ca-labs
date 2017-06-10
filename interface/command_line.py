import argparse

from component_controllers.all_components_controller import AllComponentsController
from component_controllers.bmi_controller import BMIController
from component_controllers.bmr_controller import BMRController
from component_controllers.calories_controller import CaloriesController
from interface.interface import Interface


class CommandLine(Interface):
    @staticmethod
    def _create_argparser():
        parser = argparse.ArgumentParser(
            description='If no optional arguments given calculate daily calories rate.')
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-bmr", help="calculate BMR (Basal Metabolic Rate)", action="store_true")
        group.add_argument("-bmi", help="calculate BMI (Body Mass Index)", action="store_true")
        group.add_argument("-all", help="calculate BMR, BMI and daily calories rate", action="store_true")
        return parser

    def _parse_args(self):
        """
        Parse command line arguments and instantiate the appropriate controller.
        :return: BaseComponentController subclass
        """
        args = self._create_argparser().parse_args()
        if args.bmr:
            return BMRController(self._serializer, self._view)
        if args.bmi:
            return BMIController(self._serializer, self._view)
        if args.all:
            return AllComponentsController(self._serializer, self._view)
        return CaloriesController(self._serializer, self._view)

    def launch(self):
        self._parse_args().control()