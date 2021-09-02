from queue import Queue

print("STARTING TEST")
my_queue = Queue()
my_queue.enque(6)
my_queue.enque(6)
my_queue.enque(8)
my_queue.enque(0)
my_queue.enque(0)
my_queue.enque(1)

# Test expected value
assert my_queue.__repr__() == "6 -> 6 -> 8 -> 0 -> 0 -> 1 -> None"
print("PASS Queue.__repr__()")

# Test enque()
assert my_queue.enque(5) == None
assert my_queue.__repr__() == "6 -> 6 -> 8 -> 0 -> 0 -> 1 -> 5 -> None"
print("PASS Queue.enque()")

# Test deque()
assert my_queue.deque() == 6
assert my_queue.__repr__() == "6 -> 8 -> 0 -> 0 -> 1 -> 5 -> None"
print("PASS Queue.deque()")
