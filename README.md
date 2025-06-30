```Project status: In progress - testing.```


## **Project description**
A Python calculator library written for pytest and unittest demonstration. 
The calculator covers addition, subtraction, multiplication, division, square root of a number, logarithm.
Although the calculator operations and tests basing on the same math module or operators in some cases, thus expected results should be the same and testing might find irrelevant, the purpose of the project was not the calculator itself.
Main idea was to create and run tests in both, unittest and pytest to demonstrate potency of the two and implement TDD approach that develops the calculator using tests as the main motion for ideas.
Also, some tests use math.isclose() instead of regular comparison and standard deviation error was implemented (rel_tol = 1e-9). This was done to differentiate some potential cases that could have mathematically different results due to rounding or working with large/small numbers. It would not happen in current stage of the project because the same functions and/or operators were used. However, to catch such cases beforementioned math.isclose() was used.

_TDD_ - Originally, the calculator was written with utilization of simple functions yet due to needs for further testing it was rewritten in OOP.

_Number of tests_ - 81 individual tests for unittest and pytest (162 in total). 


### Features
- Basic math operations: add, subtract, multiply, divide
- Power and square root, logarithm
- Error handling: ZeroDivisionError, ValueError, TypeError
- Assertion checks and math.isclose()

### Tech Stack
- Python 3.11+ (used 3.13)
- Pytest (used 8.4.1)
- Unittest

### Project structure
- /**calculator**
  - /**operations.py:** Calculator logic used for testing.
- /**testing_pytest**
  - /**__init__.py:** Init file required for running tests.
  - /**test_operations_pytest.py:** Testing file utilizing pytest module.
  - /**pytest_results.txt:** Text file results of pytest.
- /**testing_unittest**
  - /**__init__.py:** Init file required for running tests.
  - /**test_operations_unittest.py:** Testing file utilizing unittest.
  - /**pytest_results.txt:** Text file results of unittest.
  - /**README.md:** Readme file with project's data and description.


### How to run tests

- **Clone repository:** 
- - git clone https://github.com/twojuser/pytest_unittest_calculator.git
- - cd pytest_unittest_calculator
- **(OPTIONAL) Create venv:**
- - python -m venv .venv
- - source .venv/bin/activate
- - .venv\Scripts\activate
- **Install required packages:** pip install pytest
- **Run unittest and save results:**: python -m unittest discover testing_unittest > test_results.txt 2>&1
- **Run pytest and save results (pytest file only):** pytest testing_pytest -v > pytest_results.txt 2>&1