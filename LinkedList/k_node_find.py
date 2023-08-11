'''
find_kth_from_end

Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.
For example, let's say you want to find the item that is 3 steps away from the end of the LL. 
To do this, you would start from the head of the LL and move through the links until you reach the item that is 3 steps away from the end.

This is the problem of finding the "kth node from the end" of a linked list. 
Your task is to write a program that takes as input a linked list and a number k, and returns the item that is k steps away from the end of the list.
'''

#create 2 pointer one has the head start of k node
# Travel to the end
#return the lower node

def kth_node_from_end(linkedlist, k):
    fast = slow = linkedlist.head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow= slow.next
        fast= fast.next

    return slow
