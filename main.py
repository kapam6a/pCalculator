import sys
import StackMachine
import Parser

if len(sys.argv) < 2:
    print("Please provide expression")
    sys.exit(1)

tokens = ""
for i in range(1, len(sys.argv)):
    tokens = tokens + sys.argv[i]

tokens = tokens.strip()

if tokens[0] in ["+", "-", "/", "*"]:
    parser = Parser.PrefixNotationParser(tokens)
elif tokens[0].isnumeric() and not tokens[1].isnumeric():
    parser = Parser.InfixNotationParser(tokens)
    print(parser.parse())
else:
    parser = Parser.PostfixNotationParser(tokens)

stackMachine = StackMachine.StackMachine()
for token in parser.parse():
    if token.isnumeric():
        stackMachine.push(int(token))
    elif token == "+":
        stackMachine.add()
    elif token == "-":
        stackMachine.subtract()
    elif token == "/":
        stackMachine.divide()
    elif token == "*":
        stackMachine.multiply()
    elif token == " ":
        continue
    else:
        print("Not supported symbol")
        sys.exit(1)
print(f"{stackMachine.pop()}")
