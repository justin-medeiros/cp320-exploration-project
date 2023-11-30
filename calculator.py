class Calculator():
    def __init__(self):
        pass
    def _addition(self, val1, val2):
        return val1 + val2
    def _subtract(self, val1, val2):
        return val1 - val2
    def _multiply(self, val1, val2):
        return val1 * val2
    def _divide(self, val1, val2):
        return val1 / val2
    '''
        Function will evaluate the string expression passed
    '''
    def evaluateExpression(self, expressionString):
        operators = {'+': self._addition, '-': self._subtract, '*': self._multiply, '/': self._divide}

        # Go through all operators to find the one that is in the expression string
        for op in operators:
            if op in expressionString:
                # Seperate the values from the operation symbol
                vals = expressionString.split(op)
                try:
                    # Extract values from expression
                    val1, val2 = int(vals[0]), int(vals[1])
                    # Calculate the expression with the correct operator found
                    return operators[op](val1, val2)
                except (ValueError, IndexError):
                    return "Invalid expression"

        return "No valid operator found"

