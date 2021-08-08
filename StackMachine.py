
class StackMachine:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def add(self):
        self.applyOperation(lambda f, s: f + s)

    def subtract(self):
        self.applyOperation(lambda f, s: f - s)

    def divide(self):
        self.applyOperation(lambda f, s: f / s)

    def multiply(self):
        self.applyOperation(lambda f, s: f * s)

    def pop(self):
        return self.stack.pop()

    def applyOperation(self, f):
        secondOperand = self.stack.pop()
        firstOperand = self.stack.pop()
        self.stack.append(f(firstOperand, secondOperand))
