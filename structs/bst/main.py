from bst import Node, insert, find, delete, inorder, preorder, postorder, bfs, level_order, dfs, mirror, is_same, size, size_2, size_3, size_4, find_tree_height, min_value, max_value, find_max_path, find_min_path, root_to_leaf_path, root_to_leaf_path_sum, insert_duplicate_node, getLevel, nodes_by_level, isSymmetric, invertTree

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

# Test bfs()
expected = bfs(root)
assert expected == [5,1,6,3,10,7,100,200]
print("PASS bfs()")

# Test level_order()
rez = level_order(root)
print(rez)
assert rez == [[5],[1,6],[3,10],[7,100],[200]]
print("PASS level_order()")

# Test dfs()
depth_order = dfs(root)
assert depth_order == [5,1,3,6,10,7,100,200]
print("PASS dfs()")

# Test mirror()
tree0 = Node(4)
insert(tree0, 1)
insert(tree0, 2)
insert(tree0, 3)
insert(tree0, 6)

lista_inorder = []
inorder(tree0, lista_inorder) # [1, 2, 3, 4, 6]
lista_inorder.reverse() # [6, 4, 3, 2, 1]

mirror(tree0)
lista_inorder_mirror = []
inorder(tree0, lista_inorder_mirror) # [6, 4, 3, 2, 1]

assert lista_inorder == lista_inorder_mirror

print("PASS mirror()")

# Test is_same()
tree1 = Node(4)
insert(tree1, 1)
insert(tree1, 2)
insert(tree1, 3)
insert(tree1, 6)

tree2 = Node(4)
insert(tree2, 1)
insert(tree2, 2)
insert(tree2, 3)
insert(tree2, 6)

tree3 = Node(4)
insert(tree3, 1)
insert(tree3, 2)
insert(tree3, 9) # this is different
insert(tree3, 6)

assert is_same(tree1, tree2) == True
assert is_same(tree1, tree3) == False
assert is_same(tree2, tree3) == False

print("PASS is_same()")

# Test size()
assert size(root) == 8
print("PASS size()")

# Test size_2()
assert size_2(root) == 8
print("PASS size_2()")

# Test size_3()
assert size_3(root) == 8
print("PASS size_3()")

# Test size_4()
assert size_4(root) == 2
print("PASS size_4()")

# Test find_tree_height()
assert find_tree_height(root) == 5
print("PASS find_tree_height()")

# Test min_value()
assert min_value(root) == 1
print("PASS min_value()")

# Test max_value()
assert max_value(root) == 200
print("PASS max_value()")

# Test find_max_path()
assert find_max_path(root) == 321
print("PASS find_max_path()")

# Test find_min_path()
assert find_min_path(root) == 6
print("PASS find_min_path()")

# Test root_to_leaf_path()
current_path = []
all_paths = []
root_to_leaf_path = root_to_leaf_path(root, current_path, all_paths)
assert [[5, 1, 3], [5, 6, 10, 7], [5, 6, 10, 100, 200]] == root_to_leaf_path
print("PASS root_to_leaf_path()")

# Test root_to_leaf_path_sum()
current_path_sum = []
all_paths_sum = []
root_to_leaf_path_sum = root_to_leaf_path_sum(root, current_path_sum, all_paths_sum)
assert [9, 28, 321] == root_to_leaf_path_sum
print("PASS root_to_leaf_path_sum()")

# Test insert_duplicate_node()
insert_duplicate_node(root)
level_order = bfs(root)
assert level_order == [5, 5, 6, 1, 6, 10, 1, 3, 10, 100, 3, 7, 100, 200, 7, 200]
print("PASS insert_duplicate_node()")

# Test getLevel()
assert getLevel(root, 400) == 0
assert getLevel(root, 10) == 3
assert getLevel(root, 5) == 1
print("PASS getLevel()")

# Test isSymmetric()
assert isSymmetric(root) is False
print("PASS isSymmetric()")

# Test invertTree()
invertTree(root)
expected_backorder = []
inorder(root, expected_backorder)
assert expected_backorder == [200, 200, 100, 100, 10, 10, 7, 7, 6, 6, 5, 5, 3, 3, 1, 1]
print("PASS invertTree()")
