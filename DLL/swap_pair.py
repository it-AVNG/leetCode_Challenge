'''
DLL: Swap Nodes in Pairs (⚡Interview Question)
You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1-->2-->3-->4--> should become 2-->1-->4-->3-->

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem without modifying the values in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)

'''

def swap_pairs(self):
        #this linked list does not have a tail pointer
        dummy = Node(0)
        #dummy node points to self.head, now the head is where the dummy node is pointing at
        dummy.next = self.head
        #create a prev node to track
        prev = dummy

        #traverse until end, check if there are pairs to swap
        while self.head and self.head.next:
            #assign a node to 2 nodes that next to each other
            first_node = self.head
            second_node = self.head.next
            #Update the pointer of prev.next to second node
            prev.next = second_node
            #update the fist_node.next to the third node
            first_node.next = second_node.next
            #update the second_node.next to the first node
            second_node.next = first_node
            #update the prev pointer of the seconode to prev and first node to second node
            second_node.prev = prev #swaped
            first_node.prev = second_node #swap
            #update the pointer of the thid node if it is not None
            if first_node.next:
                first_node.next.prev = first_node
            #move the head to the third node
            self.head = first_node.next
            #move the prev to the first node
            prev = first_node
        #move the head back to the top of the list    
        self.head = dummy.next


