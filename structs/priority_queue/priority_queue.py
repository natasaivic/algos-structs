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
