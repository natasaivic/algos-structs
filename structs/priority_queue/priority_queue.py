import heapq

class PriorityQueue:
    def __init__(self):
        self.data = []

    def enque(self, element):
        heapq.heappush(self.data, element)

    def deque(self):
        return heapq.heappop(self.data)

arr = [1,1,1,1,2,2,3,3,3,3,3,3,4]

counts = {}
for n in arr:
    if n not in counts:
        counts[n] = 0
    counts[n] += 1

# add to heap
pq = PriorityQueue()
for num in counts:
    pq.enque((counts[num]*-1, num))

# take from heap
k = 2
for i in range(k):
    count, num = pq.deque()
    print(f"{num}: {count*-1}")

animals = ['cat', 'dog', 'horse', 'cat', 'squirrel', 'dog', 'squirrel', 'deer', 'dog', 'deer', 'cat', 'deer', 'horse', 'cat', 'deer', 'deer', 'pig']

# create counts
dictionary = {}
for i in animals:
  if i not in dictionary:
    dictionary[i] = 0
  dictionary[i] += 1

print(dictionary)

# add to heap 
pq1 = PriorityQueue()
for key in dictionary:
  pq1.enque((dictionary[key] * -1, key))

# take from the heap
k = 5
for i in range(k):
  count, animal = pq1.deque()
  print(f"{animal}: {count * -1}")
  