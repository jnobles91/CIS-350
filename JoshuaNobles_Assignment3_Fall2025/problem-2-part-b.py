class PostfixExpressionEvaluator():
    def __init__(self):
        #initialize a set of operators
        self.operators = set(['+','-','*','/','%','^'])



    def evaluatePostfixExpression(self,postfix):
        #initialize a stack and append a right parentheses to the postfix expression
        stack = []
        postfix = postfix + ')'
        for char in postfix:
            #iterate through the expression, if its a number convert it to an integer and push it to stack
            if char.isalnum():
                stack.append(int(char))
            #if we hit an operator do that operation on the first 2 values in the stack
            elif char in self.operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    result = num1 + num2
                elif char == '-':
                    result = num1 - num2
                elif char == '*':
                    result = num1 * num2
                elif char == '/':
                    result = num1 / num2
                elif char == '%':
                    result = num1 % num2
                elif char == '^':
                    result = num1 ** num2
                #push the result to the stack
                stack.append(result)
            # when we hit the end return result
            elif char == ')':
                return stack.pop()

evaluator = PostfixExpressionEvaluator()
postfix = '62+5*84/-' 
res = evaluator.evaluatePostfixExpression(postfix) #expect 38
print(res)