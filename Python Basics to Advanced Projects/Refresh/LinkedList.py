class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.tail = newNode
        self.head = newNode
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
