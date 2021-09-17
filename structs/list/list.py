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
        
    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def find(self, search_value):
        if self.head is None:
            return False

        current = self.head
        while current is not None:
            if current.value == search_value:
                return True
            current = current.next
        return False
    
    def find_nth(self, n):
        if self.head is None:
            return None
        current = self.head
        for i in range(1, n):
            if current is None:
                return None
            current = current.next
        return current.value
    
    def find_nth_last(self, n):
        if self.head is None:
            return None
        
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        
        current = self.head
        for i in range(0, length - n):
            current = current.next
        return current.value

    def find_middle(self):
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

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
    
    def replace(self, n, m):
        if self.head is None:
            return False
        
        current = self.head
        while current is not None:
            if current.value == n:
                current.value = m
                return True
            current = current.next
        return False

    def suma(self):
        suma = 0
        current = self.head
        while current is not None:
            suma += current.value
            current = current.next
        return suma

    def is_cyclic(self, head):
        slow = self.head
        fast = self.head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                print(f"{fast} -> {slow}")
                return True
        return False

    def __repr__(self):
        return f"{self.head}"
        