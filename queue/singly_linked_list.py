class Node:
    # initial value of Node when initialized
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    # function to get it's own value.
    def get_value(self):
        return self.value

    # function to get the next Node that is linked to this one.
    def get_next(self):
        return self.next_node

    # set this node's next_node reference to the passed in node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    # initialization of this LinkedList setting head and tail to None
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_Node = Node(value) # create a new node from the passed in value.

        # if there isnt a head set it to the new_Node made above.
        if not self.head and not self.tail:
            self.head = new_Node
            self.tail = new_Node
        else:
            # assigh previous_head to the original head.
            previous_head = self.head
            # set the head to the new_node.
            self.head = new_Node
            # set the previous head that was in position 0 to position 1 thus pushing it over after adding our new head.
            self.head.set_next(previous_head)

    def add_to_tail(self, value):
        new_Node = Node(value)
        if not self.head and not self.tail:
            self.head = new_Node
            self.tail = new_Node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            self.tail = current
            current.set_next(new_Node)

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            # value is the current value or aka current node the get_value is currently on.
            value = self.head.get_value()
            # overwriting the self.head
            self.head = self.head.get_next()
            return value

    def remove_from_tail(self):
        # if there is no head, return nothing.
        if not self.head:
            return None
        else:
            # previous head & current head are self.head
            previous = self.head
            current = self.head
            # while the get_next is still not at the tail (aka end)
            while current.get_next() is not None:
                # set "previous" to current node
                previous = current
                current = current.get_next()
            # set the previous node to the new tail since the current tail was removed.
            self.tail = previous
            previous.set_next(None)
            return current.get_value()