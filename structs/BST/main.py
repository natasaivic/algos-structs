from bst import Node, insert, find, delete

print("STARTING TEST")
root = Node(4)
insert(root, 1)
insert(root, 2)
insert(root, 3)
insert(root, 6)
insert(root, 9)
insert(root, 7)
insert(root, 5)
insert(root, 8)
insert(root, 10)
insert(root, 100)
insert(root, 200)

# Test find()
assert find(root, 4) == True
assert find(root, 9) == True
assert find(root, 200) == True
assert find(root, 15) == False
assert find(root, -1) == False
print("PASS find()")

# Test delete()
delete(root, 8) 
assert find(root, 8) == False
delete(root, 4)
assert find(root, 4) == False
delete(root, 2)
assert find(root, 2) == False
delete(root, 9)
assert find(root, 9) == False
print("PASS delete()")