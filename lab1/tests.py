from unittest import TestCase
from unittest import main

from calculator import calories_calculator, bmr_calculator, bmi_calculator


class TestCaloriesCalculator(TestCase):
    def test_male(self):
        tc = ['male', 90, 182, 19]
        self.assertAlmostEqual(bmr_calculator(*tc), 2079.80, 2)
        self.assertAlmostEqual(calories_calculator(*tc, exercise_level='Hard'), 3587.66, 2)

    def test_female(self):
        tc = ['female', 55, 164, 26]
        self.assertAlmostEqual(bmr_calculator(*tc), 1356.00, 2)
        self.assertAlmostEqual(calories_calculator(*tc, exercise_level='Moderate'), 2101.80, 2)

    def test_invalid(self):
        tc = ['mama', 89, 190, 38, 'None']
        self.assertEqual(calories_calculator(*tc), -1)
        tc = ['male', 89, 190, 38, 'Do a lot of sports']
        self.assertEqual(calories_calculator(*tc), -1)
        tc = ['male', -11, 190, 38, 'None']
        self.assertEqual(calories_calculator(*tc), -1)


class TestBMICalculator(TestCase):
    def test_valid(self):
        self.assertAlmostEqual(bmi_calculator(57, 189), 15.96, 2)

    def test_invalid(self):
        self.assertEqual(bmi_calculator(-43, 135), -1)


if __name__ == '__main__':
    main()
