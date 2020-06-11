"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

lists are stored sequentially in memory. 
the elements are stored one after the other. 
they are faster to access, but slower in addition or deletion of elements.

linked lists are not stored sequentially in memory. 
each element holds the address of the next element. 
they are slower to access but faster in addition or deletion of elrements.

in stacks, you add items to the back and remove items from the back.

"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             pass
#         else:
#             self.size -= 1
#             return self.storage.pop()

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_tail()