from stack import Stack

print("STARTING TEST")
my_stack = Stack()
my_stack.push(2)
my_stack.push(5)
my_stack.push(8)
my_stack.push(0)
my_stack.push(0)
my_stack.push(1)

# Test expected value
assert my_stack.__repr__() == "1 -> 0 -> 0 -> 8 -> 5 -> 2 -> None"
print("PASS Stack.__repr__()")

# Test push()
assert my_stack.push(7) == None
assert my_stack.__repr__() == "7 -> 1 -> 0 -> 0 -> 8 -> 5 -> 2 -> None"
print("PASS Stack.push()")

# Test pop()
assert my_stack.pop() == 7
assert my_stack.__repr__() == "1 -> 0 -> 0 -> 8 -> 5 -> 2 -> None"
assert my_stack.pop() == 1
assert my_stack.__repr__() == "0 -> 0 -> 8 -> 5 -> 2 -> None"
print("PASS Stack.pop()")