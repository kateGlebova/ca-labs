from unittest import TestCase
from unittest import main

from calculator import calories_calculator, losing_weight


class TestCaloriesCalculator(TestCase):
    def test_male(self):
        tc = ['male', 90, 182, 19, 'None']
        self.assertEqual(calories_calculator(*tc), 2079.80)

    def test_female(self):
        tc = ['female', 55, 164, 26, 'Moderate']
        self.assertEqual(calories_calculator(*tc), 2101.80)

    def test_invalid(self):
        tc = ['mama', 89, 190, 38, 'None']
        self.assertEqual(calories_calculator(*tc), -1)
        tc = ['male', 89, 190, 38, 'Do a lot of sports']
        self.assertEqual(calories_calculator(*tc), -1)
        tc = ['male', -11, 190, 38, 'None']
        self.assertEqual(calories_calculator(*tc), -1)

if __name__ == '__main__':
    main()
