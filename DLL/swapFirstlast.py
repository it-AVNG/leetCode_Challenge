'''
Instructions:
DLL: Swap First and Last (⚡Interview Question)
Swap the values of the first and last node

Method name:
swap_first_last

Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

*** Solution Explanation ***
def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value




The method swaps the values of the first and last nodes of a linked list.

The first if statement checks if the linked list is empty or has only one node. If either of these conditions is true, then the method returns without doing anything.

If the linked list has at least two nodes, then the method swaps the values of the first and last nodes using a tuple assignment. 
The tuple (self.tail.value, self.head.value) represents the values of the last and first nodes, respectively. 
The values are swapped by setting the tuple to (self.head.value, self.tail.value).

After the values are swapped, the method exits. Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

'''

def swap_first_last(self):
    # Check if the list is empty or has only one node
    if self.head is None or self.head == self.tail:
        return
    # Swap the values of the head and tail nodes
    self.head.value, self.tail.value = self.tail.value, self.head.value