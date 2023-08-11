'''
Instructions:
LL: Reverse Between (⚡Interview Question)
You are given a singly linked list and two integers m and n. 
Your task is to write a method reverse_between within 
the LinkedList class that reverses the nodes of the 
linked list from index m to index n (inclusive) in one pass and in-place.

Input

The method reverse_between takes two integer inputs m and n.
If the linked list is empty or has only one node, the method should return None.

Example

Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, 
and m = 2 and n = 4. 
Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

The reverse_between method in a LinkedList class takes two integer inputs m and n and reverses the 
linked list between the nodes located at positions m and n, inclusive.

If the linked list is empty, the method returns None.

The method first creates a dummy node with value 0 and sets its next attribute to the head of the linked list. 
Then, it sets prev to the dummy node and iterates prev m times.

At this point, prev points to the node that precedes the m-th node.
Next, the method sets current to the m-th node and iterates through the linked list n-m times.

In each iteration, the method swaps the next pointers of current and its next node, 
thereby reversing the order of the nodes between positions m and n.

The method uses a temporary variable temp to store the next node of current, which is needed to perform the swap.
Finally, the method updates the head of the linked list to the next node of the dummy node.
'''

# A method to reverse a linked list from node m to node n inclusive.
# If the linked list is empty, then return None.

import random

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class linked_list:
    def __init__(self,value = None) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        if value == None:
            self.length = 0
        else:
            self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        #traverse to the end
        #keeping track of the second-to-last Node
        while(temp.next):
            pre = temp
            temp = temp.next
        #set the tail to second-to-last
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    def reverse_between(self, m, n):    
        '''  
        # # If the linked list is empty, then return None.
        # if not self.head:
        #     return None
    
        # # create a dummy node and connect it to the head.
        # dummy = Node(0)
        # dummy.next = self.head
        # prev = dummy
    
        # # move prev to the node at position m.
        # for i in range(m):
        #     prev = prev.next
    
        # # set current to the next node of prev.
        # current = prev.next
        
        # # Reverse the linked list from position m to n.
        # for i in range(n - m):
        #     temp = current.next
        #     current.next = temp.next
        #     temp.next = prev.next
        #     prev.next = temp
    
        # # update the head of the linked list with the next node of the dummy.
        # self.head = dummy.next
        '''
      # check if linklist has one node only
        if self.head.next == None :
            return None
      #create a dummy Node and a pre node 
        dummy = Node(0)
        dummy.next = self.head
        pre = dummy
      #traverse the pre node to the node before m-th node
        for _ in range(m):
            pre = pre.next
      #set the dummy node at the m-th node
        current = pre.next
      #Reverse the linked list from position m to n.
        for i in range(n-m):
            temp = current.next
            current.next = temp.next
            temp.next = pre.next
            pre.next = temp
            




my_link = linked_list()

def ran_int_list(length):
   random_list = [random.randint(0, 100) for _ in range(length)]
   print(random_list)
   return random_list

ran_int = ran_int_list(13)
for num in ran_int:
    my_link.append(num)

my_link.reverse_between(2,8)
my_link.print_list()