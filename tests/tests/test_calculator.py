import pytest
from calculator.calculator import Calculation, AdvancedCalculator

def test_addition():
    calc = Calculation(5, 3)
    assert calc.add() == 8

def test_subtraction():
    calc = Calculation(5, 3)
    assert calc.subtract() == 2

def test_multiplication():
    calc = Calculation(5, 3)
    assert calc.multiply() == 15

def test_division():
    calc = Calculation(6, 2)
    assert calc.divide() == 3

def test_divide_by_zero():
    calc = Calculation(6, 0)
    assert calc.divide() == "Cannot divide by zero"

def test_calculation_history():
    calc1 = Calculation(10, 5)
    calc1.add()
    calc2 = Calculation(20, 10)
    calc2.subtract()
    
    Calculation.add_to_history(calc1)
    Calculation.add_to_history(calc2)
    
    assert len(Calculation.history()) == 2

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 5, 8),
    (10, 2, 12),
    (7, 3, 10)
])
def test_addition_with_parametrization(num1, num2, expected):
    calc = Calculation(num1, num2)
    assert calc.add() == expected

