'''
Insertion at the Beginning of a Singly Linked List
Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are already provided.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.value
        self.tail = self.tail
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            