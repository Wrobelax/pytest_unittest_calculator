"""Testing operations by using pytest."""

# Importing calculator 'operations' and pytest module.
import pytest
from calculator import operations as calc

# Creating test cases for addition.
def test_add():
    assert calc.add(5, 8) == 13
    
def test_add_negative():
    assert calc.add(4, -1) == 3

def test_add_zero():
    assert calc.add(9, 0) == 9


# Creating test cases for subtraction.
def test_subtract():
    assert calc.subtract(5, 2) == 3

def test_subtract_negative():
    assert calc.subtract(3, 6) == -3

def test_subtract_negative_number():
    assert calc.subtract(7, -2) == 9


# Creating test cases for multiplication.
def test_multiply():
    assert calc.multiply(4, 4) == 16

def test_multiply_zero():
    assert calc.multiply(0,8) == 0

def test_multiply_negative():
    assert calc.multiply(7, -2) == -14


# Creating test cases for division.
def test_divide():
    assert calc.divide(8, 2) == 4

def test_divide_negative():
    assert calc.divide(5, -5) == -1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(4, 0)


# Creating test cases for power raising.
def test_power():
    assert calc.power(5, 2) == 25

def test_power_zero():
    assert calc.power(8, 0) == 1

def test_power_negative():
    assert calc.power(-2, 3) == -8


# Creating test cases for square root of a number.
def test_sqrt():
    assert calc.sqrt(16) == 4

def test_sqrt_zero():
    assert calc.sqrt(0) == 0

def test_sqrt_negative():
    with pytest.raises(ValueError):
        calc.sqrt(-3)