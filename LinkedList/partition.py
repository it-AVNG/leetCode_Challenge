'''
Instructions:

LL: Partition List (⚡Interview Question)

You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).
You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition.
the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. 

You should preserve the original relative order of the nodes in each of the two partitions.
You need to implement this method as a method of the LinkedList class. 
The method should take an integer x as input. If the linked list is empty, the method should return None.
To implement this method, you should create two new linked lists. 
These two linked lists will be made up of the original nodes from the linked list that is being partitioned, 
one for nodes less than x and one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.
The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning process).
You should then traverse the original linked list and append each node to the appropriate new linked list.
Finally, you should connect the two new linked lists together.

'''

def partition_list(self,x):
    small = linked_list()
    large = linked_list()
    temp = self.head
    while (temp.next):
        if temp.value < x:
            small.append(temp.value)
        else:
            large.append(temp.value)
    #connect the end of small to the head of large
    temp = small.head
    while(temp.next):
        temp = temp.next
    temp.next= large.head    