# a class in python to evaluate reverse polish notation.
from stacksQueuesTrees import Stack
import operator
import math

class RPN():

    def __init__(self) -> None:
        self.stack = Stack
        # a dictionary with keys for all operations. uses a python module for operators as functions.
        operDict = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,'^':operator.pow,'sin':math.sin,'tan':math.tan,'cos':math.cos,'pi':math.pi}

    def numberTest(self, x):
        # I used StackOverflow
        # checks if it's a number value
        try:
            float(x)
            return True
        except ValueError:
            return False

    def precedence(oper):
        """checks precedence of characters and returns a value for infix postfix translation"""
        if oper == '+' or oper == '-':
            return 1
        elif oper == '*' or oper == '/':
            return 2
        elif oper == '**':
            return 3
    
    def evaluate(self, postfix):
        """evaluates postfix statements to a value"""
        # this splits the equation into bits based on spaces
        splitPostfix = postfix.split(' ')
        for char in splitPostfix:
            # If we encounter an operand 
            if numberTest(char) == True:
                # it goes into the stack
                self.stack.push(char)
            #If we counter an operator
            else:
                # ensures enough operands in stack
                if len(self.stack)<2:
                    # if not evaluation is done and returns final value
                    self.stack.top()
                else:
                    #Pop topmost item to the right of the operator
                    #Nextmost item is popped to the left of the operator
                    operand1 = self.stack.POP()
                    operand2 = self.stack.POP()
                    #Calculate evaluation
                    calc = self.operDict[char](operand1,operand2)
                    #Add evaluation of the equation to the top of the stack
                    self.stack.push(calc)
        
                

    def infixToPostfix(x):
        pass

RPN = RPN()
RPN.evaluate("357++")