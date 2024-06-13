from models.operation import Operation

class Calculator:
    def __init__(self):
        self.operation = Operation()

    def add(self, a, b):
        """Add two numbers"""
        return self.operation.add(a, b)

    def subtract(self, a, b):
        """Subtract two numbers"""
        return self.operation.subtract(a, b)

    def multiply(self, a, b):
        """Multiply two numbers"""
        return self.operation.multiply(a, b)

    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return self.operation.divide(a, b)