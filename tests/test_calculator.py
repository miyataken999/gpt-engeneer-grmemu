import pytest
from src.calculator import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 2) == 3

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(4, 5) == 20

def test_divide():
    calculator = Calculator()
    assert calculator.divide(10, 2) == 5.0

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.divide(10, 0)