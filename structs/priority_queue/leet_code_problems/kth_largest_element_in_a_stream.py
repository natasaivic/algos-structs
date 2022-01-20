# 703. Kth Largest Element in a Stream
import heapq

class KthLargest:
    def __init__(self, k: int, nums: []):
        self.k = k
        self.heap = [] 
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)   
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


expected = []
kth = KthLargest(3,[4,5,8,2])

expected.append(kth.add(3))
expected.append(kth.add(5))
expected.append(kth.add(10))
expected.append(kth.add(9))
expected.append(kth.add(4))

print(expected)