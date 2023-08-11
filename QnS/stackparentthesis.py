'''
Instructions:
Stack: Parentheses Balanced (⚡Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. 
For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. 
On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  
Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and 
return True if it is balanced, or 
False if it is not. In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.

'''
def is_balance_parentthesis(strs):
    my_stack = Stack()
    for character in strs:
        #chec if character is an open parent thesis
        if character == '(':
          my_stack.push(character)
        #if it is a close thesis, check if the previous thesis is open
        elif character == ')':
            if my_stack.ist_empty() or my_stack.pop() != '(':
                #if not or it is empty, return false
                return False
    #if there are remaining single parentthesis, return false            
    return my_stack.ist_empty

class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self,value):
        self.stack_list.append(value)
    #pop element using pop method from string
    # def pop(self):
    #     return self.stack.pop()
    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i])
    def peek(self):
        if self.stack_list.ist_empty():
            return None
        #return top of the stack
        return self.stack_list[-1]
    def ist_empty(self):
        return len(self.size()) == 0
    def size(self):
        return len(self.stack_list)
    



