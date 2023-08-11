#Create a constructor for Class Stack that implements a new stack with an empty list.
#create a method to print stack
class stack:
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

    