'''
Instructions:
Queue Using Stacks: Dequeue (⚡Interview Question)
You have been tasked with implementing a queue data structure using two stacks in Python, and you need to write the dequeue method.

The dequeue method should remove and return the first element in the queue.

*** Solution Explanation ***
def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.stack1.pop()




This code is the implementation of the dequeue method for a queue data structure implemented using two stacks.

The purpose of the dequeue method is to remove and return the first element in the queue. In this implementation, the first element is always at the bottom of stack1.

The code first checks if the queue is empty using the is_empty method. If the queue is empty, the method returns None because there are no elements to remove.

If the queue is not empty, the method removes and returns the last element in stack1 using the pop method. This is because the first element in the queue is always at the bottom of stack1, and pop removes elements from the end of a list.

Overall, this implementation of dequeue is efficient because it only requires popping elements from stack1. Any elements that were moved to stack2 during the enqueue operation are moved back to stack1 before the next dequeue operation, so there is no need to access stack2 in this method.





Code with inline comments:

'''





class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
    #da code
    def dequeue(self):
    # Check if the queue is empty
      if self.is_empty():
        # Return None if the queue is empty
        return None
      else:
        # Remove and return the last element in stack1
        # which is the first element in the queue
        return self.stack1.pop()
    

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Dequeue some values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Enqueue another value
q.enqueue(4)

# Output the front of the queue again
print("Front of the queue:", q.peek())

# Dequeue all remaining values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

# Dequeue from an empty queue and check if it returns None
print("Dequeued value from empty queue:", q.dequeue())

