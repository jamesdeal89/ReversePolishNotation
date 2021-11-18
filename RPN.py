# a class in python to evaluate reverse polish notation.
from stacksQueuesTrees import Stack
import operator
import math

class RPN():

    def __init__(self) -> None:
        self.stack = Stack
        # a dictionary with keys for all operations
        operDict = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.div,'^':operator.pow,'sin':math.sin,'tan':math.tan,'cos':math.cos,'pi':math.pi}

    def numberTest(self, x):
        # I used StackOverflow
        # checks if it's a number value
        try:
            float(x)
            return True
        except ValueError:
            return False

    def precedence(oper):
        """checks precedence of characters and returns a value"""
        if oper == '+' or oper == '-':
            return 1
        elif oper == '*' or oper == '/':
            return 2
        elif oper == '**':
            return 3
    
    def evaluate(self, postfix):
        # this splits the equation into bits based on spaces
        splitPostfix = postfix.split(' ')
        for char in splitPostfix:
            # If we encounter an operand 
            if numberTest(char) == True:
                # it goes into the stack
                self.stack.push(char)
            else:
                # ensures enough operands in stack
                if len(self.stack)<2:
                    break
                else:
                    operand1 = self.stack.POP()
                    operand2 = self.stack.POP()
                    calc = self.operDict[char](operand1,operand2)
                    self.stack.push(calc)
                


            #If we counter an operator 
                #Pop topmost item to the right of the operator
                    #Nextmost item is popped to the left of the operator
                        #Rewrite entire stack without last two values
                            #Add evaluation of the equation to the top of the stack


    def infixToPostfix(x):
        pass