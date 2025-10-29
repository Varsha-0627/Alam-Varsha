class Calculator:
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

if _name_ == "_main_":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add/subtract/multiply/divide): ").lower()

    calc = Calculator(a, b)
    result = calc.calculate(operation)
    print("Result:", result)