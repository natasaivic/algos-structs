class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)

    if node.value == value:
        return node

    if value > node.value:
        node.right = insert(node.right, value)
    else:
        node.left = insert(node.left, value)
    return node

def find(node, value):
    if node is None:
        return False
    
    if node.value == value:
        return True
    
    if value > node.value:
        return find(node.right, value)
    else:
        return find(node.left, value)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, value):
    if node is None:
        return None

    if node.value == value:
        if node.left is None and node.right is None:
            return None
        if node.left is not None and node.right is None:
            return node.left
        if node.left is None and node.right is not None:
            return node.right
        
        temp = find_min(node.right)
        node.value = temp.value
        node.right = delete(node.right, temp.value)
        return node

    if value > node.value:
        node.right = delete(node.right, value)
    else:
        node.left = delete(node.left, value)
    return node

def inorder(node, lista_nodova):
    if node is None:
        return

    if node.left is not None:
        inorder(node.left, lista_nodova)

    lista_nodova.append(node.value)

    if node.right is not None:
        inorder(node.right, lista_nodova)

def preorder(node, lista_nodova):
    if node is None:
        return

    lista_nodova.append(node.value)

    if node.left is not None:
        preorder(node.left, lista_nodova)

    if node.right is not None:
        preorder(node.right, lista_nodova)

def postorder(node, lista_nodova):
    if node is None:
        return

    if node.left is not None:
        postorder(node.left, lista_nodova)

    if node.right is not None:
        postorder(node.right, lista_nodova)
        
    lista_nodova.append(node.value)

def bfs(node):
    level_order = []
    queue = []
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        level_order.append(node.value)
    return level_order

def dfs(node): # preorder, left to right traversal using stack data structure
    depth_order = []
    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        depth_order.append(node.value)
    return depth_order

def mirror(node):
    if node is None:
        return node
    
    temp = node.left
    node.left = node.right
    node.right = temp

    if node.left is not None:
        mirror(node.left)
    if node.right is not None:
        mirror(node.right)

def is_same(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is None:
        return False
    elif root1 is None and root2 is not None:
        return False
    else:
        if (root1.value == root2.value and is_same(root1.left, root2.left) and is_same(root1.right, root2.right)):
            return True
        else:
            return False

# Counts the number of nodes in a binary search tree, 
# top down, using recursion. 
def size(node):
    if node is None:
        return 0
    count = 1
    count += size(node.left)
    count += size(node.right)
    return count

# Counts the number of nodes in a binary 
# search tree, bottom up, using recursion.
def size_2(node): 
    if node is None:
        return 0
    return 1 + size_2(node.left) + size_2(node.right)

# Counts the number of nodes in a binary search tree, 
# using queue data structure.
def size_3(node): 
    if node is None:
        return 0
    queue = []
    queue.append(node)
    count = 0
    while len(queue) > 0:
        node = queue.pop(0)
        count += 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return count

# Counts the number of nodes without leaf nodes 
# in a binary search tree, using queue data structure.
def size_4(node):
    if node is None:
        return 0
    queue = []
    queue.append(node)
    count = 0
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left is not None and node.right is not None:
            count += 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return count

# Count the number of nodes along the longest path 
# from the root node down to the farthest leaf node
def find_tree_height(node):
    if node is None:
        return 0
    left_height = find_tree_height(node.left)
    right_height = find_tree_height(node.right)
    return max(left_height, right_height) + 1

# Find the node with minimum value in a Binary Search Tree
def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value

def find_max_path(node):
    if node is None:
        return 0
    left_sum = find_max_path(node.left)
    right_sum = find_max_path(node.right)
    return max(left_sum, right_sum) + node.value

def find_min_path(node):
    if node is None:
        return 0
    left_sum = find_min_path(node.left)
    right_sum = find_min_path(node.right)
    return min(left_sum, right_sum) + node.value

def root_to_leaf_path(node, current_path, all_paths):
    current_path.append(node.value)
    if node.left is None and node.right is None:
        all_paths.append(current_path.copy())
    if node.left is not None:
        root_to_leaf_path(node.left, current_path, all_paths)
    if node.right is not None:
        root_to_leaf_path(node.right, current_path, all_paths)
    current_path.pop()
    return all_paths

def suma(values):
    s = 0
    for value in values:
        s += value
    return s

def root_to_leaf_path_sum(node, current_path, all_paths):
    current_path.append(node.value)
    if node.left is None and node.right is None:
        all_paths.append(suma(current_path))
    if node.left is not None:
        root_to_leaf_path_sum(node.left, current_path, all_paths)
    if node.right is not None:
        root_to_leaf_path_sum(node.right, current_path, all_paths)
    current_path.pop()
    return all_paths

# doubleTree()
# For each node in a binary search tree, create a new duplicate node, 
# and insert the duplicate as the left child of the original node. 
def insert_duplicate_node(node):
    if node is None:
        return None

    insert_duplicate_node(node.left)
    insert_duplicate_node(node.right)

    duplicate_value = node.value
    duplicate_node = Node(duplicate_value)
    temp = node.left
    node.left = duplicate_node
    duplicate_node.left = temp
    return node
