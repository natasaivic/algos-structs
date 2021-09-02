class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
            return

        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.top is None:
            return None
        
        temp = self.top.value
        self.top = self.top.next
        return temp

    def __repr__(self):
        return f"{self.top}"