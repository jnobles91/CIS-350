class InfixtoPostfixConverter():
    
    def __init__(self):
        #create a dictionary of presedence for use with the presedence and operator methods
        self.operator_map = {'+' :1, '-' :1,'*' :2,'/' :2,'%' :2,'^' :3}

    def is_operator(self,item):
        #check if item is in our dictionary of operators
        return item in self.operator_map.keys()
    
    def precedence(self,item):
        #if an item is in our operator dictionary return its presedence, else return 0
        if self.is_operator(item):
            return self.operator_map[item]
        else:
            return 0
        
    def converttoPostfix(self,infix):
        #add a parentheses to the end of the infix expression
        infix = infix + ')'
        #start the stack with a left perentheses
        stack = ['(']
        postfix = []
        for char in infix:
            #iterate through the infix expression, first checking if its a number
            if char.isalnum():
                #if it is add it to the postfix expression
                postfix.append(char)
            elif self.is_operator(char) == True:
                #when we hit an operator start adding to the postfix while their presedence is less than the current operator 
                while (stack and self.is_operator(stack[-1]) and
                    ((self.precedence(char) <= self.precedence(stack[-1])))):
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == '(':
                #if we hit a left perentheses add it to the stack
                stack.append(char)
            elif char == ')':
                #if we hit a right perentheses start adding operators until we hit a left perentheses 
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop() #then remove that left perentheses
        
        while stack:
            #add any remaining operators to postfix
            postfix.append(stack.pop())

        #convert the postfix list to a string and return
        return ' '.join(postfix)
    
converter = InfixtoPostfixConverter()

infix  = '(6+2)*5-8/4'
postfix = converter.converttoPostfix(infix)
print(postfix)






    


    
