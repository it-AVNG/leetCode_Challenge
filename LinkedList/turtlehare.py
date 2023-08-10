# return the linked list middle without using length attribute
import LinkedList 
import random
my_link = LinkedList.linked_list()

def ran_int_list(length):
   random_list = [random.randint(0, 100) for _ in range(length)]
   print(random_list)
   return random_list

ran_int = ran_int_list(13)
for num in ran_int:
    my_link.append(num)

turle = my_link.head
hare = my_link.head

while(hare!= None and hare.next != None):
    turle = turle.next
    hare = hare.next.next

print(turle.value)
