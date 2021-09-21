import hashlib

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucket = [None] * 1000

    # Inserts a key-value pair into the hash map. 
    # If the value already exists in the hash map, update the value.
    def put(self, key, value):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            self.bucket[index] = Item(key, value)
            return
        
        current = self.bucket[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        item = Item(key, value)
        item.next = self.bucket[index]
        self.bucket[index] = item
    
    # Returns the value to which the specified key is mapped, 
    # or “No record found” if this map contains no mapping for the key.
    def get(self, key):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            return None
        
        current = self.bucket[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None

    # Removes the mapping for the specific key 
    # if the hash map contains the mapping for the key.
    def delete(self, key):
        index = hash(key) % len(self.bucket)

        if self.bucket[index] is None:
            return False
        
        if self.bucket[index].key == key:
            self.bucket[index] = self.bucket[index].next
            return True
        
        previous = self.bucket[index]
        current = self.bucket[index].next
        while current is not None:
            if current.key == key:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False
