import unittest
from simple_calculator.py import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(1, 22), 23)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(3, 2), 1)
        self.assertEqual(self.calc.subtraction(40, 30), 10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 2), 14)
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(40, 3), 120)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(20, 10), 2)
        with self.assertRaises(ZeroErrorDivision):
            self.calc.divide(10, 0)
