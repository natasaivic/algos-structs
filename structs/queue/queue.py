class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"
    
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    def enque(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
            return
        
        self.back.next = node
        self.back = node
    
    def deque(self):
        if self.front is None:
            return None
        
        temp = self.front.value
        self.front = self.front.next
        return temp
    
    def __repr__(self):
        return f"{self.front}"