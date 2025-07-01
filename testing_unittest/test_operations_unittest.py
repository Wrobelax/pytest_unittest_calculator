"""Testing operations by using unittest."""

# Importing calculator 'operations' for testing and unittest module.
from calculator.operations import Calculator
import unittest
import math



# Creating class for testing.
class TestOperations(unittest.TestCase):


# Creating setUp instance for calculator object.
    def setUp(self):
        self.calc = Calculator()



# Creating test cases for addition.
    def test_add(self):
        test_cases = [
            (5, 8, 13),
            (12, 6, 18),
            (30, 1, 31),
            (1, 2, 3),
            (9, 19, 28)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_negative(self):
        test_cases = [
            (-5, -8, -13),
            (-12, -6, -18),
            (-30, -1, -31),
            (-1, -2, -3),
            (-9, -19, -28)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_zero(self):
        test_cases = [
            (5, 0, 5),
            (0, 6, 6),
            (0, 1, 1),
            (1, 0, 1),
            (9, 0, 9)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_large_number(self):
        test_cases = [
            (1e308, 1e308, 2e616),
            (2e308, 1e309, 3e617),
            (3e900, 6e099, 9e999),
            (2e00, 2e00, 4e00),
            (8e340, 1e220, 9e560)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_small_negative(self):
        test_cases = [
            (1, -1e-10, 0.9999999999),
            (2, -1e-008, 1.99999999),
            (3, -1e-05, 2.99999),
            (8, -1e-02, 7.99),
            (5, -1e-11, 4.99999999999)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_same_numbers(self):
        test_cases = [
            (1, 1, 2),
            (17, 17, 34),
            (55, 55, 110),
            (29, 29, 58),
            (43, 43, 86)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_int_float(self):
        test_cases = [
            (5, 2.3, 7.3),
            (4, 8.8, 12.8),
            (5, 1.1, 6.1),
            (2, 2.9, 4.9),
            (7, 7.7, 14.7)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_float_int(self):
        test_cases = [
            (5.1, 2, 7.1),
            (4.4, 8, 12.4),
            (5.1, 1, 6.1),
            (2.9, 2, 4.9),
            (7.7, 7, 14.7)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)


    def test_add_string_first(self):
        test_cases = [
            ("33", 33),
            ("8", 8),
            ("55", 55),
            ("7", 7),
            ("57", 57)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.add(a, b)


    def test_add_string_second(self):
        test_cases = [
            (33, "33"),
            (8, "8"),
            (55, "55"),
            (7, "7"),
            (57, "57")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.add(a, b)


    def test_add_none_first(self):
        test_cases = [
            (None, 33),
            (None, 8),
            (None, 55),
            (None, 7),
            (None, 57)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.add(a, b)


    def test_add_none_second(self):
        test_cases = [
            (33, "33"),
            (8, "8"),
            (55, "55"),
            (7, "7"),
            (57, "57")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.add(a, b)



# Creating test cases for subtraction.
    def test_subtract(self):
        test_cases = [
            (13, 5, 8),
            (17, 7, 10),
            (22, 20, 2),
            (8, 1, 7),
            (51, 47, 4)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_negative(self):
        test_cases = [
            (13, 15, -2),
            (17, 71, -54),
            (22, 26, -4),
            (1, 8, -7),
            (47, 54, -7)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_negative_number(self):
        test_cases = [
            (13, -15, 28),
            (17, -71, 88),
            (22, -26, 48),
            (1, -8, 9),
            (47, -54, 101)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_same_numbers(self):
        test_cases = [
            (13, 13, 0),
            (17, 17, 0),
            (22, 22, 0),
            (1, 1, 0),
            (47, 47, 0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_zero(self):
        test_cases = [
            (13, 0, 13),
            (17, 0, 17),
            (22, 0, 22),
            (1, 0, 1),
            (47, 0, 47)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_small_number(self):
        self.assertEqual(self.calc.subtract(1, 1e-15), 0.999999999999999)
        test_cases = [
            (1, 1e-15, 0.999999999999999),
            (2, 1e-15, 1.999999999999999),
            (4, 2e-22, 4.0),
            (5, 5e-11, 4.99999999995),
            (8, 4e-02, 7.96)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_int_float(self):
        test_cases = [
            (8, 3.3, 4.7),
            (6, 2.2, 3.8),
            (4, 2.4, 1.6),
            (5, 1.1, 3.9),
            (8, 3.24, 4.76)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_float_int(self):
        test_cases = [
            (7.8, 2, 5.8),
            (9.9, 5, 4.9),
            (4.8, 1, 3.8),
            (5.8, 2, 3.8),
            (8.76, 4, 4.76)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_subtract_minuend_string(self):
        test_cases = [
            ("33", 23),
            ("6", 4),
            ("18", 1),
            ("27", 2),
            ("2", 12)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.subtract(a, b)

    def test_subtract_subtrahend_string(self):
        test_cases = [
            (33, "23"),
            (6, "4"),
            (18, "1"),
            (27, "2"),
            (2, "12")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.subtract(a, b)

    def test_subtract_minuend_none(self):
        test_cases = [
            (None, 23),
            (None, 4),
            (None, 1),
            (None, 2),
            (None, 12)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.subtract(a, b)

    def test_subtract_subtrahend_none(self):
        test_cases = [
            (33, None),
            (6, None),
            (18, None),
            (27, None),
            (2, None)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.subtract(a, b)



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

    def test_multiply_float_int(self):
        self.assertEqual(self.calc.multiply(0.2, 7), 1.4000000000000001)

    def test_multiply_quotient_string(self):
        with self.assertRaises(TypeError):
            self.calc.multiply("24", 12)

    def test_multiply_ratio_string(self):
        with self.assertRaises(TypeError):
            self.calc.multiply(24, "12")

    def test_multiply_quotient_none(self):
        with self.assertRaises(TypeError):
            self.calc.multiply(None, 12)

    def test_multiply_ratio_none(self):
        with self.assertRaises(TypeError):
            self.calc.multiply(24, None)


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

    def test_divide_float_int(self):
        self.assertEqual(self.calc.divide(5.5, 5), 1.1)

    def test_divide_dividend_string(self):
        with self.assertRaises(TypeError):
            self.calc.divide("5", 6)

    def test_divide_divider_string(self):
        with self.assertRaises(TypeError):
            self.calc.divide(8, "9")

    def test_divide_dividend_none(self):
        with self.assertRaises(TypeError):
            self.calc.divide(None, 9)

    def test_divide_divider_none(self):
        with self.assertRaises(TypeError):
            self.calc.divide(3, None)


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
        result = self.calc.power(2.3, 2.2)
        expected = math.pow(2.3, 2.2)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_power_int_float(self):
        result = self.calc.power(2, 1.1)
        expected = math.pow(2, 1.1)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_power_float_int(self):
        result = self.calc.power(1.1, 2)
        expected = math.pow(1.1, 2)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_power_string(self):
        with self.assertRaises(TypeError):
            self.calc.power("3",8)

    def test_power_of_string(self):
        with self.assertRaises(TypeError):
            self.calc.power(8, "9")

    def test_power_none(self):
        with self.assertRaises(TypeError):
            self.calc.power(None, 6)

    def test_power_of_none(self):
        with self.assertRaises(TypeError):
            self.calc.power(6, None)


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
        result = self.calc.sqrt(1e308)
        expected = math.sqrt(1e308)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_sqrt_small_number(self):
        result = self.calc.sqrt(1e-308)
        expected = math.sqrt(1e-308)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_sqrt_string(self):
        with self.assertRaises(TypeError):
            self.calc.sqrt("5")

    def test_sqrt_none(self):
        with self.assertRaises(TypeError):
            self.calc.sqrt(None)


# Creating test cases for a logarithm of a number.
    def test_logarithm(self):
        result = self.calc.logarithm(3, 2)
        expected = math.log(3, 2)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_no_argument(self):
        result = self.calc.logarithm(4)
        expected = math.log(4)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_zero(self):
        with self.assertRaises(ValueError):
            self.calc.logarithm(0,4)

    def test_logarithm_negative(self):
        with self.assertRaises(ValueError):
            self.calc.logarithm(-2, 3)

    def test_logarithm_base_zero(self):
        with self.assertRaises(ValueError):
            self.calc.logarithm(5, 0)

    def test_logarithm_base_one(self):
        with self.assertRaises(ValueError):
            self.calc.logarithm(6,1)

    def test_logarithm_large(self):
        result = self.calc.logarithm(1e308, 2e089)
        expected = math.log(1e308, 2e089)
        self.assertTrue(math.isclose(result, expected, rel_tol=1e-9))

    def test_logarithm_small(self):
        result = self.calc.logarithm(1e-308)
        expected = math.log(1e-308)
        self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_string(self):
        with self.assertRaises(TypeError):
            self.calc.logarithm("3", 5)

    def test_logarithm_base_string(self):
        with self.assertRaises(TypeError):
            self.calc.logarithm(5, "9")

    def test_logarithm_none(self):
        with self.assertRaises(TypeError):
            self.calc.logarithm(None, 4)