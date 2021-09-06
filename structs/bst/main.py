from bst import Node, insert, find, delete, inorder, preorder, postorder

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

# Test inorder()
lista_inorder = []
inorder(root, lista_inorder)
assert lista_inorder == [1, 3, 5, 6, 7, 10, 100, 200]
print("PASS inorder()")

# Test preorder()
lista_preorder = []
preorder(root, lista_preorder)
assert lista_preorder == [5, 1, 3, 6, 10, 7, 100, 200]
print("PASS preorder()")

# Test postorder()
lista_postorder = []
postorder(root, lista_postorder)
assert lista_postorder == [3, 1, 7, 200, 100, 10, 6, 5]
print("PASS postorder()")
