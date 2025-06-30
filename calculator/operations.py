"""Calculator class for testing operations."""


# Importing math module.
import math


# Creating general class for orchestrating all operations.
# Adding validation for data type.
class Calculator:
    def _validate_number(self, value):
        if not isinstance(value,(int, float)):
            raise TypeError(f"Incorrect data type. Expected int or float, got {type(value).__name__}")
        else:
            return value


# Creating basic operations.
    def add(self, a, b):
        self._validate_number(a)
        self._validate_number(b)
        return a + b

    def subtract(self, a, b):
        self._validate_number(a)
        self._validate_number(b)
        return a - b

    def multiply(self, a, b):
        self._validate_number(a)
        self._validate_number(b)
        return a * b

    def divide(self, a, b):
        self._validate_number(a)
        self._validate_number(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by 0!")
        return a / b

    def power(self, a, b):
        self._validate_number(a)
        self._validate_number(b)
        return a ** b

    def sqrt(self, a):
        self._validate_number(a)
        if a < 0:
            raise ValueError("Cannot take a square root of a negative number!")
        return math.sqrt(a)