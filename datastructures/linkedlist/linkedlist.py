
class LinkedList:

    class Node:

        def __init__(self, data, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
    
    def size(self):
        if self.empty():
            return 0
        else:
            count = 0
            node = self.head
            while node.data != None:
                count += 1
                node = node.next
            return 0

    def empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def value_at(self, index):
        if self.empty():
            return None
        else:
            ind = 0
            node = self.head
            while ind < index:
                node = node.next
                ind += 1
            return node.data
    
    def push_front(self, value):
        oldHead = self.head
        newNode = LinkedList.Node(value, oldHead)
        self.head = newNode
    
    def pop_front(self):
        if self.empty():
            return None
        else:
            newHead = self.head.next
            data = self.head.data
            self.head = newHead
            return data
    
    def push_back(self, value):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = LinkedList.Node(value)

    def pop_back(self):
        node = self.head
        while node.next is not None:
            node = node.next
        data = node.next.data
        node.next = None
        return data
    
    def front(self):
        return self.head.data

    def back(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node.data

    def insert(self, index, value):
        node = self.head
        ind = 0
        while ind < index:
            node = node.next
            ind += 1
        newNode = LinkedList.Node(value, node.next)
        node.next = newNode

    def erase(self, index):
        node = self.head
        ind = 0
        while ind < index - 1:
            node = node.next
            ind += 1
        node.next = node.next.next

    def print_all(self):
        node = self.head
        i = 0
        while node is not None:
            print("Node %s: %s" % (i, node.data))
            node = node.next
            i += 1
        