import hashlib
class Node_s:
  def __init__(self, key):
    self.key = key
    self.next = None

class Set:
  def __init__(self):
    self.bucket = [None] * 100

  def add(self, key):
    index = hash(key) % len(self.bucket)
    if self.bucket[index] is None:
      self.bucket[index] = Node_s(key)
      return

    current = self.bucket[index]
    while current is not None:
      if current.key == key:
        return
      current = current.next
    
    node = Node_s(key)
    node.next = self.bucket[index]
    self.bucket[index] = node

  def remove(self, key):
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

  def exists(self, key):
    index = hash(key) % len(self.bucket)
    if self.bucket[index] is None:
      return False

    current = self.bucket[index]
    while current is not None:
      if current.key == key:
        return True
      current = current.next
    
    return False