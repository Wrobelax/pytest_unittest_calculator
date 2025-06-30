"""Testing operations by using pytest."""

# Importing calculator 'operations' and pytest module.
import pytest
from pytest_unittest_calculator.calculator.operations import Calculator


# Adding pytest fixture for calculator object.
@pytest.fixture
def calc():
    return Calculator()

# Creating test cases for addition.
def test_add(calc):
    assert calc.add(5, 8) == 13
    
def test_add_negative(calc):
    assert calc.add(4, -1) == 3

def test_add_zero(calc):
    assert calc.add(9, 0) == 9

def test_add_large_number(calc):
    assert calc.add(1e308, 1e308) == 2e616

def test_add_small_negative(calc):
    assert calc.add(1.0, -1e-10) == 0.9999999999

def test_add_same_numbers(calc):
    assert calc.add(17, 17) == 34

def test_add_int_float(calc):
    assert calc.add(5, 3.8) == 8.8


# Creating test cases for subtraction.
def test_subtract(calc):
    assert calc.subtract(5, 2) == 3

def test_subtract_negative(calc):
    assert calc.subtract(3, 6) == -3

def test_subtract_negative_number(calc):
    assert calc.subtract(7, -2) == 9

def test_subtract_same_numbers(calc):
    assert calc.subtract(9, 9) == 0

def test_subtract_zero(calc):
    assert calc.subtract(13, 0) == 13

def test_subtract_small_number(calc):
    assert calc.subtract(1, 1e-15) == 0.999999999999999

def test_subtract_int_float(calc):
    assert calc.subtract(7, 2.8) == 4.2


# Creating test cases for multiplication.
def test_multiply(calc):
    assert calc.multiply(4, 4) == 16

def test_multiply_zero(calc):
    assert calc.multiply(0,8) == 0

def test_multiply_negative(calc):
    assert calc.multiply(7, -2) == -14

def test_multiply_one(calc):
    assert calc.multiply(3, 1) == 3

def test_multiply_large(calc):
    assert calc.multiply(2e013, 3e18) == 6e+31

def test_multiply_floats(calc):
    assert calc.multiply(3.2, 0.5) == 1.6

def test_multiply_int_float(calc):
    assert calc.multiply(7, 0.2) == 1.4000000000000001


# Creating test cases for division.
def test_divide(calc):
    assert calc.divide(8, 2) == 4

def test_divide_negative(calc):
    assert calc.divide(6, -3) == -2

def test_divide_zero(calc):
    assert calc.divide(0, 5) == 0

def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(4, 0)

def test_divide_one(calc):
    assert calc.divide(13, 1) == 13

def test_divide_same_numbers(calc):
    assert calc.divide(7,7) == 1

def test_divide_float(calc):
    assert calc.divide(1.0, 3.0) == 0.3333333333333333

def test_divide_int_float(calc):
    assert calc.divide(7, 2.5) == 2.8


# Creating test cases for power raising.
def test_power(calc):
    assert calc.power(5, 2) == 25

def test_power_by_zero(calc):
    assert calc.power(8, 0) == 1

def test_power_zero(calc):
    assert calc.power(0,7) == 0

def test_power_negative(calc):
    assert calc.power(-2, 3) == -8

def test_power_one(calc):
    assert calc.power(0, 0) == 1

def test_power_floats(calc):
    assert calc.power(2.3, 2.2) == 6.248866394748044

def test_power_int_float(calc):
    assert calc.power(2, 1.1) == 2.1435469250725863


# Creating test cases for square root of a number.
def test_sqrt(calc):
    assert calc.sqrt(16) == 4

def test_sqrt_zero(calc):
    assert calc.sqrt(0) == 0

def test_sqrt_negative(calc):
    with pytest.raises(ValueError):
        calc.sqrt(-3)

def test_sqrt_one(calc):
    assert calc.sqrt(1) == 1

def test_sqrt_float(calc):
    assert calc.sqrt(4.0) == 2.0

def test_sqrt_large_number(calc):
    assert calc.sqrt(1e308) == 1e+154

def test_sqrt_small_number(calc):
    assert calc.sqrt(1e-308) == 1e-154