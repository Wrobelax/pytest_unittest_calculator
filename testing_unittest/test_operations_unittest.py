"""Testing operations by using unittest."""

# Importing calculator 'operations' for testing and unittest module.
from pytest_unittest_calculator.calculator.operations import Calculator
import unittest



# Creating class for testing.
class TestOperations(unittest.TestCase):

# Creating setUp instance for calculator object.
    def setUp(self):
        self.calc = Calculator()


# Creating test cases for addition.
    def test_add(self):
        self.assertEqual(self.calc.add(2,3), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -3), -4)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_add_large_number(self):
        self.assertEqual(self.calc.add(1e308, 1e308), 2e616)

    def test_add_small_negative(self):
        self.assertEqual(self.calc.add(1.0, -1e-10), 0.9999999999)

    def test_add_same_numbers(self):
        self.assertEqual(self.calc.add(17, 17),34)

    def test_add_int_float(self):
        self.assertEqual(self.calc.add(5, 3.8), 8.8)


# Creating test cases for subtraction.
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8,5), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(3, 9), -6)

    def test_subtract_negative_number(self):
        self.assertEqual(self.calc.subtract(9, -3), 12)

    def test_subtract_same_numbers(self):
        self.assertEqual(self.calc.subtract(9, 9), 0)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(13, 0), 13)

    def test_subtract_small_number(self):
        self.assertEqual(self.calc.subtract(1, 1e-15), 0.999999999999999)

    def test_subtract_int_float(self):
        self.assertEqual(self.calc.subtract(7, 2.8),4.2)


# Creating test cases for multiplication.
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(3, -3), -9)

    def test_multiply_one(self):
        self.assertEqual(self.calc.multiply(3, 1), 3)

    def test_multiply_large(self):
        self.assertEqual(self.calc.multiply(2e013, 3e18), 6e+31)

    def test_multiply_floats(self):
        self.assertEqual(self.calc.multiply(3.2, 0.5), 1.6)

    def test_multiply_int_float(self):
        self.assertEqual(self.calc.multiply(7, 0.2), 1.4000000000000001)


# Creating test cases for division.
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6, 0)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(0,5), 0)

    def test_divide_one(self):
        self.assertEqual(self.calc.divide(13, 1), 13)

    def test_divide_same_numbers(self):
        self.assertEqual(self.calc.divide(7,7), 1)

    def test_divide_float(self):
        self.assertEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

    def test_divide_int_float(self):
        self.assertEqual(self.calc.divide(7, 2.5), 2.8)


# Creating test cases for power raising.
    def test_power(self):
        self.assertEqual(self.calc.power(3, 2), 9)

    def test_power_by_zero(self):
        self.assertEqual(self.calc.power(7, 0), 1)

    def test_power_zero(self):
        self.assertEqual(self.calc.power(0,8), 0)

    def test_power_negative(self):
        self.assertEqual(self.calc.power(-2, 3), -8)

    def test_power_one(self):
        self.assertEqual(self.calc.power(0, 0), 1)

    def test_power_floats(self):
        self.assertEqual(self.calc.power(2.3, 2.2), 6.248866394748044)

    def test_power_int_float(self):
        self.assertEqual(self.calc.power(2, 1.1), 2.1435469250725863)


# Creating test cases for square root of a number.
    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)

    def test_sqrt_zero(self):
        self.assertEqual(self.calc.sqrt(0), 0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            self.calc.sqrt(-5)

    def test_sqrt_one(self):
        self.assertEqual(self.calc.sqrt(1), 1)

    def test_sqrt_float(self):
        self.assertEqual(self.calc.sqrt(4.0), 2.0)

    def test_sqrt_large_number(self):
        self.assertEqual(self.calc.sqrt(1e308),1e+154)

    def test_sqrt_small_number(self):
        self.assertEqual(self.calc.sqrt(1e-308), 1e-154)