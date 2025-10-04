import unittest
from simple_calculator.py import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()

    def Test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(1, 22), 23)

    def Test_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(3, 2), 1)
        self.assertEqual(self.calc.subtraction(40, 30), 10)

    def Test_multiplication(self):
        self.assertEqual(self.calc.multiplication(7, 2), 14)
        self.assertEqual(self.calc.multiplication(3, 5), 15)
        self.assertEqual(self.calc.multiplication(40, 3), 120)

    def Test_division(self):
        self.assertEqual(self.calc.division(6, 2), 3)
        self.assertEqual(self.calc.division(20, 10), 2)
        with self.assertRaises(ZeroErrorDivision):
            self.calc.division(10, 0)
