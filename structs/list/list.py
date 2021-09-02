class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"

class List:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
    
    def find(self, search_value):
        if self.head is None:
            return False

        current = self.head
        while current is not None:
            if current.value == search_value:
                return True
            current = current.next
        return False
    
    def delete(self, value):
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        previous = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next
        return False
    
    def is_empty(self):
        return self.head is None
    
    def __repr__(self):
        return f"{self.head}"