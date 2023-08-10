'''
Instructions:
LL: Has Loop (⚡Interview Question)
Write a method called has_loop that is part of the linked list class.(done)
The method should be able to detect if there is a cycle or loop present in the linked list.
The method should utilize Floyd's cycle-finding algorithm, 
also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
The method should follow these guidelines:

1. Create two pointers, slow and fast, both initially pointing to the head of the linked list.
2. Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
3. If there is a loop in the list, the fast pointer will eventually meet the slow pointer. 
If this occurs, the method should return True.
4. If the fast pointer reaches the end of the list or encounters a None value, 
it means there is no loop in the list. In this case, the method should return False.
'''

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

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        
        return False



my_link = linked_list()
ran_int = [1,2,3,4,3,2,5]
for num in ran_int:
    my_link.append(num)
my_link.print_list()