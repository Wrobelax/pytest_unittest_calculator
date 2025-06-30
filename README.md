```Project status: In progress - testing.```


## **Project description**
A simple Python calculator library written for pytest and unittest demonstration. 
The project utilizes TDD (test-driven development) and parametrization.

_TDD_ - Originally, the calculator was written with utilization of simple functions yet due to needs for further testing it was rewritten in OOP.



### Features
- Basic math operations: add, subtract, multiply, divide
- Power and square root
- Error handling: ZeroDivisionError, ValueError

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
- **Run pytest and save results (pytest file only):** pytest testing_pytest -v > pytest_results.tzxt 2>&1