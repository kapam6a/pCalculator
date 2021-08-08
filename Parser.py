
class PrefixNotationParser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        print(self.tokens)
        return self.tokens


class InfixNotationParser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.currentIndex = 0
        self.result = []
        self.operators = []

    def parse(self):
        while not self.isEnd():
            currentToken = self.tokens[self.currentIndex]
            self.currentIndex += 1
            if currentToken.isnumeric():
                self.result.append(currentToken)
            elif len(self.operators) == 0:
                self.operators.append(currentToken)
            elif self.precedence(self.operators[-1]) < self.precedence(currentToken):
                self.operators.append(currentToken)
            else:
                self.result.append(self.operators.pop())
                self.operators.append(currentToken)

        while len(self.operators) != 0:
            operator = self.operators.pop()
            self.result.append(operator)

        return self.result

    def isEnd(self):
        return self.currentIndex + 1 > len(self.tokens)

    def precedence(self, operator):
        if operator in ["+", "-"]:
            return 0
        elif operator in ["/", "*"]:
            return 1

class PostfixNotationParser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        return self.tokens

