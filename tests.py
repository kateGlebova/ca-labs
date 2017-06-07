from unittest import TestCase
from unittest import main

from calculation.calculator import Calculator


class TestCaloriesCalculator(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_male(self):
        tc = ['male', 90, 182, 19]
        self.assertAlmostEqual(self.calculator.bmr_calculator(*tc), 2079.80, 2)
        self.assertAlmostEqual(self.calculator.calories_calculator(*tc, exercise_level='Hard'), 3587.66, 2)

    def test_female(self):
        tc = ['female', 55, 164, 26]
        self.assertAlmostEqual(self.calculator.bmr_calculator(*tc), 1356.00, 2)
        self.assertAlmostEqual(self.calculator.calories_calculator(*tc, exercise_level='Moderate'), 2101.80, 2)

    def test_invalid(self):
        tc = ['mama', 89, 190, 38, 'None']
        self.calories_invalid(*tc)
        tc = ['male', 89, 190, 38, 'Do a lot of sports']
        self.calories_invalid(*tc)
        tc = ['male', -11, 190, 38, 'None']
        self.calories_invalid(*tc)
        tc = ['female', 11, -190, 38, 'None']
        self.calories_invalid(*tc)

    def calories_invalid(self, *tc):
        with self.assertRaises(ValueError):
            self.calculator.calories_calculator(*tc)


class TestBMICalculator(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_valid(self):
        self.assertAlmostEqual(self.calculator.bmi_calculator(57, 189), 15.96, 2)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.calculator.bmi_calculator(-43, 135)


if __name__ == '__main__':
    main()
