# test_calculator.py

from Calculator import add, subtract, multiply, divide, Calculation

# Test the operations
print(add(5, 3))        # 8
print(subtract(5, 3))   # 2
print(multiply(5, 3))   # 15
print(divide(6, 3))     # 2.0
print(divide(6, 0))     # Error: Division by zero

# Test the Calculation class
calc = Calculation(10)
calc.add_to_history("Add 5 + 5", 10)
print(calc.get_history())  # ["Add 5 + 5: 10"]

