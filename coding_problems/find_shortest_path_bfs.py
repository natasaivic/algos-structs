class Node:
  def __init__(self, value, price):
    self.value = value
    self.next = None
    self.price = price 

class LinkedList:
  def __init__(self):
    self.head = None

  def get_head(self):
    return self.head

  def is_empty(self):
    if self.head is None:  
      return True
    return False
    
  def insert_at_head(self, value, price):
    temp_node = Node(value, price)
    if self.is_empty():
      self.head = temp_node
      return self.head

    temp_node.next = self.head
    self.head = temp_node
    return self.head

  def insert_at_tail(self, value, price):
    new_node = Node(value, price)
    if self.get_head() is None:
      self.head = new_node
      return
    temp = self.get_head()
    while temp.next is not None:
      temp = temp.next
    temp.next = new_node
    return


class MyQueue:
  def __init__(self):
    self.queue_list = []
    self.queue_size = 0

  def is_empty(self):
    return self.queue_size == 0

  def front(self):
    if self.is_empty():
      return None
    return self.queue_list[0]

  def enqueue(self, value):
    self.queue_size += 1
    self.queue_list.append(value)

  def dequeue(self):
    if self.is_empty():
      return None
    front = self.front()
    self.queue_list.remove(self.front())
    self.queue_size -= 1
    return front


class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.array = []
    for i in range(vertices):
      self.array.append(LinkedList())

  def add_edge(self, source, destination, price):
    if (source < self.vertices and destination < self.vertices):
      self.array[source].insert_at_head(destination, price) 

def find_shortest_path_dfs(g, a, b):
  min_price = 1000000

  visited = [False] * g.vertices
  for n in range(g.vertices):
    visited[n] = False
  
  stack = []
  stack.append(a)

  price_stack = [0]
  while len(stack) != 0:
      current_node = stack.pop()
      current_price = price_stack.pop()
      if visited[current_node] is True:
        continue
     
      if current_node == b:
        if current_price < min_price: 
          min_price = current_price
        continue

      child = g.array[current_node].head
      while child is not None:
          stack.append(child.value)
          price_stack.append(current_price + child.price)
          child = child.next
      
      visited[current_node] = True

  return min_price


def find_shortest_path_bfs(g, a, b):
  min_path = g.vertices + 1
  visited = [False] * g.vertices
  for n in range(g.vertices):
    visited[n] = False
  
  queue = MyQueue()
  queue.enqueue(a)

  path_count = 0
  in_curr_level = 1
  in_next_level = 0
  while queue.is_empty() is not True:
      if in_curr_level == 0:
        in_curr_level = in_next_level
        in_next_level = 0
        path_count += 1

      current_node = queue.dequeue()
      if visited[current_node] is True:
        continue
     
      if current_node == b:
        return path_count

      child = g.array[current_node].head
      while child is not None:
          queue.enqueue(child.value)
          child = child.next
          in_next_level += 1
      
      in_curr_level -= 1
      visited[current_node] = True

  return min_path

if __name__ == "__main__" :
  g = Graph(7)
  g.add_edge(1, 2, 100)
  g.add_edge(1, 3, 150)
  g.add_edge(2, 4, 70)
  g.add_edge(4, 5, 110)
  g.add_edge(2, 5, 190)
  g.add_edge(5, 6, 200)
  g.add_edge(3, 6, 500)

  print(find_shortest_path_dfs(g, 1, 5))
