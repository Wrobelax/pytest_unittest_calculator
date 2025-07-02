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
        test_cases = [
            (2, 3, 6),
            (17, 1, 17),
            (2, 8, 16),
            (5, 5, 25),
            (7, 9, 63)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_zero(self):
        test_cases = [
            (2, 0, 0),
            (0, 1, 0),
            (0, 8, 0),
            (5, 0, 0),
            (7, 0, 0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_negative(self):
        test_cases = [
            (-2, -2, 4),
            (9, -3, -27),
            (-6, -6, 36),
            (5, -7, -35),
            (7, -7, -49)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_one(self):
        test_cases = [
            (2, 1, 2),
            (9, 1, 9),
            (1, 6, 6),
            (1, 7, 7),
            (1, 14, 14)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_large(self):
        test_cases = [
            (2e013, 3e18, 6e+31),
            (5e089, 1e089, 5e+178),
            (2e70, 2e05, 4.0000000000000005e+75),
            (6e55, 1e90, 6e+145),
            (4e20, 1e30, 4e+50)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)


    def test_multiply_floats(self):
        test_cases = [
            (2.1, 1.2, 2.52),
            (9.3, 3.1, 28.830000000000002),
            (6.2, 5.3, 32.86),
            (3.4, 7.8, 26.52),
            (4.4, 9.2, 40.48)
         ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_int_float(self):
        test_cases = [
            (2, 1.4, 2.8),
            (9, 1.9, 17.099999999999998),
            (3, 6.3, 18.9),
            (6, 4.4, 26.400000000000002),
            (7, 3.9, 27.3)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_float_int(self):
        test_cases = [
            (0.2, 7, 1.4000000000000001),
            (9.1, 9, 81.89999999999999),
            (3.5, 2, 7),
            (4.2, 7, 29.400000000000002),
            (5.2, 8, 41.6)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_multiply_quotient_string(self):
        test_cases = [
            ("23", 7),
            ("450", 9),
            ("32", 2),
            ("65", 8),
            ("96", 65)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.multiply(a, b)

    def test_multiply_ratio_string(self):
        test_cases = [
            (2, "45"),
            (9, "34"),
            (4, "21"),
            (3, "78"),
            (2, "45")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.multiply(a, b)

    def test_multiply_quotient_none(self):
        test_cases = [
            (None, 7),
            (None, 9),
            (None, 2),
            (None, 8),
            (None, 65)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.multiply(a, b)

    def test_multiply_ratio_none(self):
        test_cases = [
            (2, None),
            (17, None),
            (2, None),
            (5, None),
            (7, None)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.multiply(a, b)



# Creating test cases for division.
    def test_divide(self):
        test_cases = [
            (6, 2, 3),
            (17, 1, 17),
            (24, 3, 8),
            (49, 5, 9.8),
            (19, 5, 3.8)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_negative(self):
        test_cases = [
            (6, -2, -3),
            (17, -1, -17),
            (-24, 3, -8),
            (-49, -5, 9.8),
            (19, -5, -3.8)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_by_zero(self):
        test_cases = [
            (6, 0),
            (17, 0),
            (-24, 0),
            (49, 0),
            (19, 0)
        ]
        for a, b in test_cases:
            with self.assertRaises(ZeroDivisionError):
                self.calc.divide(a, b)

    def test_divide_zero(self):
        test_cases = [
            (0, 6, 0),
            (0, 3, 0),
            (0, 9, 0),
            (0, 45, 0),
            (0, 32, 0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_one(self):
        test_cases = [
            (6, 1, 6),
            (17, 1, 17),
            (-4, 1, -4),
            (49, 1, 49),
            (19, 1, 19)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_same_numbers(self):
        test_cases = [
            (6, 6, 1),
            (17, 17, 1),
            (1, 1, 1),
            (49, 49, 1),
            (19, 19, 1)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_float(self):
        test_cases = [
            (1.0, 3.0, 0.3333333333333333),
            (3.0, 1.0, 3.0),
            (6.2, 1.1, 5.636363636363636),
            (5.8, 2.0, 2.9),
            (7.9, 3.4, 2.3235294117647058823529411764706)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_int_float(self):
        test_cases = [
            (1, 3.0, 0.3333333333333333),
            (3, 1.0, 3.0),
            (6, 1.1, 5.454545454545454),
            (5, 2.6, 1.923076923076923),
            (7, 3.5, 2.0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_float_int(self):
        test_cases = [
            (1.0, 3, 0.3333333333333333),
            (3.0, 1, 3.0),
            (6.2, 2, 3.1),
            (5.5, 8, 0.6875),
            (7.3, 4, 1.825)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_dividend_string(self):
        test_cases = [
            ("1", 3),
            ("3", 1),
            ("6", 2),
            ("5", 8),
            ("7", 4)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.divide(a, b)

    def test_divide_divider_string(self):
        test_cases = [
            (1, "3"),
            (3, "1"),
            (6, "2"),
            (5, "8"),
            (7, "4")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.divide(a, b)

    def test_divide_dividend_none(self):
        test_cases = [
            (None, 7),
            (None, 9),
            (None, 2),
            (None, 8),
            (None, 65)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.divide(a, b)

    def test_divide_divider_none(self):
        test_cases = [
            (2, None),
            (17, None),
            (2, None),
            (5, None),
            (7, None)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.divide(a, b)



# Creating test cases for power raising.
    def test_power(self):
        test_cases = [
            (3, 2, 9),
            (2, 3, 8),
            (4, 7, 16384),
            (12, 1, 12),
            (5, 2, 25)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.power(a, b), expected)

    def test_power_by_zero(self):
        test_cases = [
            (7, 0, 1),
            (5, 0, 1),
            (4, 0, 1),
            (12, 0, 1),
            (5, 0, 1)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.power(a, b), expected)

    def test_power_zero(self):
        test_cases = [
            (0, 1, 0),
            (0, 4, 0),
            (0, 15, 0),
            (0, 34, 0),
            (0, 9, 0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.power(a, b), expected)

    def test_power_negative(self):
        test_cases = [
            (-3, 2, 9),
            (-2, 3, -8),
            (-4, -4, 0.00390625),
            (-12, -1, -0.08333333333333333),
            (-5, 2, 25)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a = a, b = b):
                self.assertEqual(self.calc.power(a, b), expected)

    def test_power_one(self):
        self.assertEqual(self.calc.power(0, 0), 1)

    def test_power_floats(self):
        test_cases = [
            (2.3, 2.2),
            (3.5, 2.8),
            (6.7, 5.6),
            (9.1, 3.4),
            (8.7, 7.3)
            ]
        for a, b in test_cases:
            with self.subTest(a = a, b = b):
                result = self.calc.power(a, b)
                expected = math.pow(a, b)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_power_int_float(self):
        test_cases = [
            (2, 2.2),
            (3, 2.8),
            (6, 5.6),
            (9, 3.4),
            (8, 7.3)
            ]
        for a, b in test_cases:
            with self.subTest(a = a, b = b):
                result = self.calc.power(a, b)
                expected = math.pow(a, b)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_power_float_int(self):
        test_cases = [
            (2.3, 2),
            (3.5, 5),
            (6.7, 7),
            (9.1, 3),
            (8.7, 9)
            ]
        for a, b in test_cases:
            with self.subTest(a = a, b = b):
                result = self.calc.power(a, b)
                expected = math.pow(a, b)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_power_string(self):
        test_cases = [
            ("1", 3),
            ("3", 1),
            ("6", 2),
            ("5", 8),
            ("7", 4)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.power(a, b)

    def test_power_of_string(self):
        test_cases = [
            (1, "3"),
            (3, "1"),
            (6, "2"),
            (5, "8"),
            (7, "4")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.power(a, b)

    def test_power_none(self):
        test_cases = [
            (None, 7),
            (None, 9),
            (None, 2),
            (None, 8),
            (None, 65)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.power(a, b)

    def test_power_of_none(self):
        test_cases = [
            (2, None),
            (17, None),
            (2, None),
            (5, None),
            (7, None)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.power(a, b)



# Creating test cases for square root of a number.
    def test_sqrt(self):
        test_cases = [2, 3, 6, 9, 8]
        for a in test_cases:
            with self.subTest(a = a):
                result = self.calc.sqrt(a)
                expected = math.sqrt(a)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_sqrt_zero(self):
        self.assertEqual(self.calc.sqrt(0), 0)

    def test_sqrt_negative(self):
        test_cases = [-5, -3, -18, -19, -4]
        for a in test_cases:
            with self.assertRaises(ValueError):
                self.calc.sqrt(a)

    def test_sqrt_one(self):
        self.assertEqual(self.calc.sqrt(1), 1)

    def test_sqrt_float(self):
        test_cases = [2.0, 3.2, 6.7, 9.1, 8.8]
        for a in test_cases:
            with self.subTest(a = a):
                result = self.calc.sqrt(a)
                expected = math.sqrt(a)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_sqrt_large_number(self):
        test_cases = [1e308, 3e302, 6e065, 9e111, 8e043]
        for a in test_cases:
            with self.subTest(a = a):
                result = self.calc.sqrt(a)
                expected = math.sqrt(a)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_sqrt_small_number(self):
        test_cases = [1e-308, 3e-302, 6e-065, 9e-111, 8e-043]
        for a in test_cases:
            with self.subTest(a = a):
                result = self.calc.sqrt(a)
                expected = math.sqrt(a)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_sqrt_string(self):
        test_cases = ["5", "3", "18", "19", "4"]
        for a in test_cases:
            with self.assertRaises(TypeError):
                self.calc.sqrt(a)

    def test_sqrt_none(self):
        with self.assertRaises(TypeError):
            self.calc.sqrt(None)



# Creating test cases for a logarithm of a number.
    def test_logarithm(self):
        test_cases = [
            (2, 3),
            (6, 9),
            (8, 4),
            (9, 9),
            (12, 7)
        ]
        for a, b in test_cases:
            with self.subTest(a = a, b = b):
                result = self.calc.logarithm(a, b)
                expected = math.log(a, b)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_no_argument(self):
        test_cases = [2, 3, 6, 9, 12]
        for a in test_cases:
            with self.subTest(a = a):
                result = self.calc.logarithm(a)
                expected = math.log(a)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_zero(self):
        test_cases = [
            (0, 3),
            (0, 9),
            (0, 4),
            (0, 9),
            (0, 7)
        ]
        for a, b in test_cases:
            with self.assertRaises(ValueError):
                self.calc.logarithm(a, b)

    def test_logarithm_negative(self):
        test_cases = [
            (-2, 3),
            (-6, 9),
            (-8, 4),
            (-9, 9),
            (-12, 7)
        ]
        for a, b in test_cases:
            with self.assertRaises(ValueError):
                self.calc.logarithm(a, b)

    def test_logarithm_base_zero(self):
        test_cases = [
            (3, 0),
            (9, 0),
            (4, 0),
            (7, 0),
            (10, 0)
        ]
        for a, b in test_cases:
            with self.assertRaises(ValueError):
                self.calc.logarithm(a, b)

    def test_logarithm_base_one(self):
        test_cases = [
            (2, 1),
            (6, 1),
            (8, 1),
            (9, 1),
            (12, 1)
        ]
        for a, b in test_cases:
            with self.assertRaises(ValueError):
                self.calc.logarithm(a, b)

    def test_logarithm_large(self):
        test_cases = [
            (2e309, 3e034),
            (6e515, 9e002),
            (8e404, 4e200),
            (9e013, 9e321),
            (1e308, 7e308)
        ]
        for a, b in test_cases:
            with self.subTest(a = a, b = b):
                result = self.calc.logarithm(a, b)
                expected = math.log(a, b)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_small(self):
        test_cases = [1e-308, 3e-304, 2e-002, 3e-105, 1e-004]
        for a in test_cases:
            with self.subTest(a = a):
                result = self.calc.logarithm(a)
                expected = math.log(a)
                self.assertTrue(math.isclose(result, expected, rel_tol = 1e-9))

    def test_logarithm_string(self):
        test_cases = [
            ("1", 3),
            ("3", 1),
            ("6", 2),
            ("5", 8),
            ("7", 4)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.logarithm(a, b)

    def test_logarithm_base_string(self):
        test_cases = [
            (1, "3"),
            (3, "1"),
            (6, "2"),
            (5, "8"),
            (7, "4")
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.logarithm(a, b)

    def test_logarithm_none(self):
        test_cases = [
            (None, 7),
            (None, 9),
            (None, 2),
            (None, 8),
            (None, 65)
        ]
        for a, b in test_cases:
            with self.assertRaises(TypeError):
                self.calc.logarithm(a, b)