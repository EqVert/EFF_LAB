class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    # Калькулятор не має методів для множення та ділення

# підклас AdvancedCalculator, який буде розширювати функціональність базового класу BasicCalculator,
# додаючи методи для множення та ділення
class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

calculator = AdvancedCalculator()
print("Addition: ", calculator.add(5, 3))
print("Subtraction: ", calculator.subtract(5, 3))
print("Multiplication: ", calculator.multiply(5, 3))
print("Division: ", calculator.divide(5, 3))