from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        head, ret = self.head, []
        while head:
            ret.append(str(head))
            head = head.next
        return '->'.join(ret)

    # Adds node to end of linked list in O(1)
    def add_to_head(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Adds node to end of linked list in O(1)
    def add_to_tail(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def remove_first(self, target):
        head, prev = self.head, None
        while head:
            if head.data == target:
                if prev:
                    prev.next = head.next
                    if not prev.next:
                        self.tail = prev
                else:
                    head = head.next
                    
            prev = head
            head = head.next

    # Returns boolean of if the linked list contains the target
    def contains(self, target):
        head = self.head
        while head:
            if head.data == target:
                return True
            head = head.next
        return False

    # Return the index of the first occurrence of the target, and -1 if not found
    def first_index(self, target):
        head, index = self.head, 0
        while head:
            if head.data == target:
                return index
            head = head.next
            index += 1
        return -1
