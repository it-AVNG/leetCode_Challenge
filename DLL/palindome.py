'''
Instructions:
DLL: Palindrome Checker (⚡Interview Question)
Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.

Method name:
is_palindrome

'''
def is_palindrome(self):
        if self.length <= 1:
            return True
        forward_node = self.head
        backward_node = self.tail
        for i in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True