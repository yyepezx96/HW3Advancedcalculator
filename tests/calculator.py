class Calculation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = None

    # Instance method to perform arithmetic operations
    def add(self):
        self.result = self.num1 + self.num2
        return self.result

    def subtract(self):
        self.result = self.num1 - self.num2
        return self.result

    def multiply(self):
        self.result = self.num1 * self.num2
        return self.result

    def divide(self):
        try:
            if self.num2 == 0:
                raise ValueError("Cannot divide by zero")
            self.result = self.num1 / self.num2
            return self.result
        except ValueError as e:
            return str(e)

    # Class method to maintain calculation history
    calculation_history = []

    @classmethod
    def history(cls):
        return cls.calculation_history

    # Class method to add to history
    @classmethod
    def add_to_history(cls, calc_instance):
        cls.calculation_history.append(calc_instance)

    # Static method to create a calculation instance
    @staticmethod
    def create_calculation(num1, num2):
        return Calculation(num1, num2)


# This class will help to test calculations
class AdvancedCalculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

