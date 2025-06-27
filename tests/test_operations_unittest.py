"""Testing operations by using unittest."""

# Importing calculator 'operations' for testing and unittest module.
import pytest_unittest_calculator.calculator.operations as calc
import unittest



# Creating class for testing.
class TestOperations(unittest.TestCase):


# Creating test cases for addition.
    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)

    def test_add_negative(self):
        self.assertEqual(calc.add(-1, -3), -4)

    def test_add_zero(self):
        self.assertEqual(calc.add(5, 0), 5)


# Creating test cases for subtraction.
    def test_subtract(self):
        self.assertEqual(calc.subtract(8,5), 3)

    def test_subtract_negative(self):
        self.assertEqual(calc.subtract(3, 9), -6)

    def test_subtract_negative_number(self):
        self.assertEqual(calc.subtract(9, -3), 12)


# Creating test cases for multiplication.
    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 3), 12)

    def test_multiply_zero(self):
        self.assertEqual(calc.multiply(7, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(calc.multiply(3, -3), -9)


# Creating test cases for division.
    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(calc.divide(3, -3), -1)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc.divide(6, 0)


# Creating test cases for power raising.
    def test_power(self):
        self.assertEqual(calc.power(3, 2), 9)

    def test_power_zero(self):
        self.assertEqual(calc.power(7, 0), 1)

    def test_power_negative(self):
        self.assertEqual(calc.power(-2, 3), -8)


# Creating test cases for square root of a number.
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(9), 3)

    def test_sqrt_zero(self):
        self.assertEqual(calc.sqrt(0), 0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            calc.sqrt(-5)



