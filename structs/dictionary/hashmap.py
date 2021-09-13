import hashlib

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashmap:
    def __init__(self):
        self.bucket = [None] * 1000

    def put(self, key, value):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            self.bucket[index] = Item(key, value)
            return
        
        current = self.bucket[index]
        while current.next is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        if current.key == key:
            current.value = value
            return
        current.next = Item(key, value)
    
    def get(self, key, value):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            return None
        
        current = self.bucket[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
