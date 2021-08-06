import sys

if len(sys.argv) < 2:
    print("Please provide expression")
    sys.exit(1)

tokens = ""
for i in range(1, len(sys.argv)):
    tokens = tokens + sys.argv[i]

def applyOperation(f):
    secondOperand = stack.pop()
    firstOperand = stack.pop()
    stack.append(f(firstOperand, secondOperand))

stack = []
for token in tokens:
    if token.isnumeric():
        stack.append(int(token))
    elif token == "+":
        applyOperation(lambda f, s: f + s)
    elif token == "-":
        applyOperation(lambda f, s: f - s)
    elif token == "/":
        applyOperation(lambda f, s: f / s)
    elif token == "*":
        applyOperation(lambda f, s: f * s)
    elif token == " ":
        continue
    else:
        print("Not supported symbol")
        sys.exit(1)
if len(stack) != 1:
    print("Wrong expression")
    sys.exit(1)
print(f"{stack.pop()}")
