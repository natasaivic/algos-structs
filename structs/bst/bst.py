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

# Recursive function for inorder tree traversal
def inorder(node, node_list):
    if node is None:
        return

    inorder(node.left, node_list)
    node_list.append(node.value)
    inorder(node.right, node_list)

def inorder_2(node):
    if node is None:
        return []

    return inorder_2(node.left) + [node.value] + inorder_2(node.right)

# Iterative function for inorder tree traversal
def inorder_iterative(node):
    depth_order = []
    stack = []
    current = node

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
            depth_order.append(current.value)
            current = current.right
        else:
            break
    
    return depth_order

# Recursive function for preorder tree traversal
def preorder(node, node_list):
    if node is None:
        return

    node_list.append(node.value)
    preorder(node.left, node_list)
    preorder(node.right, node_list)

def preorder_2(node):
    if node is None:
        return []

    return [node.value] + preorder_2(node.left) + preorder_2(node.right)

# Iterative preorder, left to right traversal using stack data structure
def dfs(root): 
    if root is None:
        return []

    depth_order = []
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        depth_order.append(node.value)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        
    return depth_order

# Recursive function for postorder tree traversal
def postorder(node, node_list):
    if node is None:
        return

    postorder(node.left, node_list)
    postorder(node.right, node_list)  
    node_list.append(node.value)

def postorder_2(node):
    if node is None:
        return []
    
    return postorder_2(node.left) + postorder_2(node.right) + [node.value]

# Iterative postorder traversal using stack data structure
def postorder_iterative(root):
    if root is None:
        return []

    depth_order = [] 
    stack = [] 
    stack.append(root)
  
    while len(stack) > 0: 
        current = stack.pop() 
        depth_order.append(current.value)
        if current.left is not None: 
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    
    # while depth_order:
    #     print(depth_order.pop(), end=' ')
    postorder =[]
    while depth_order:
        postorder.append(depth_order.pop())
    return postorder 

def bfs(node):
    if node is None:
        return []

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

# Binary Tree Level Order Traversal 
# returns the level order traversal of its nodes' values, level by level

def level_order(node):
    if node is None:
        return []

    all_levels = []
    queue = []
    queue.append(node)
    while len(queue) > 0:
        by_level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            by_level.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        all_levels.append(by_level)

    return all_levels

def mirror(node):
    if node is None:
        return
    
    temp = node.left
    node.left = node.right
    node.right = temp

    mirror(node.left)
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
        return False

def is_same_tree(root, subRoot):
    if root is None and subRoot is None:
        return True
    elif root is None or subRoot is None:
        return False
    if root.value == subRoot.value:
        return is_same_tree(root.left, subRoot.left) and is_same_tree(root.right, subRoot.right)
        
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

# Iterative method to find height of Binary Tree
def findTreeHeight(node):
  if node is None:
    return 0

  queue = []
  queue.append(node)
  height = 0

  while(True):
    nodeCount = len(queue) # nodeCount(queue size) indicates number of nodes at current level
    if nodeCount == 0:
      return height

    height += 1
    while nodeCount > 0:
      current = queue.pop(0)
      if current.left is not None:
          queue.append(current.left)
      if current.right is not None:
          queue.append(current.right)
      nodeCount -= 1

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

# iterative 
def binaryTreePaths(node):
    res = []
    stack = []
    stack.append((node, ""))
    while len(stack) > 0:
        current, path = stack.pop()
        if current.left is None and current.right is None:
            res.append(path+str(current.value))
        
        if current.left is not None:
            stack.append((current.left, path+str(current.value)+"->"))
        if current.right is not None:
            stack.append((current.right, path+str(current.value)+"->"))

    return res

# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals targetSum.
def hasPathSum(node, targetSum):
    if node is None:
        return False

    stack = []
    stack.append((node, node.value))
    while len(stack) > 0:
        (current, sum) = stack.pop()

        if current.right is None and current.left is None:
            if sum == targetSum:
                return True
        
        if current.left is not None:
            stack.append((current.left, sum + current.left.value))

        if current.right is not None:
            stack.append((current.right, sum + current.right.value))
    
    return False

def sumOfLeftLeaves(node):
    if node is None:
        return

    sum = 0
    stack = []
    stack.append((node, False))
    while len(stack) > 0:
        (current, is_left) = stack.pop()
        if is_left is True:
            sum += current.value
        
        if current.left is not None:
            stack.append((current.left, True))
        
        if current.right is not None:
            stack.append((current.right, False))
    return sum

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

# Get Level of a node
# helper function for getlevel()
def getLevelHelper(node, value, level):
    if node is None:
        return 0
    elif node.value == value:
        return level
    elif value > node.value:
        return getLevelHelper(node.right, value, level + 1)
    else:
        return getLevelHelper(node.left, value, level + 1)

def getLevel(node, value):
    return getLevelHelper(node, value, 1)

# Get all nodes by level of a binary tree
def nodes_by_level(node):
    if node is None:
        return

    queue = []
    queue.append(node)

    elements = 0
    max_current_level = 1
    next_level_elements = 0
    current_level = []
    while len(queue) > 0:
        node = queue.pop(0)

        current_level.append(node.value)
        elements += 1

        if node.left is not None:
            queue.append(node.left)
            next_level_elements += 1
        if node.right is not None:
            next_level_elements += 1
            queue.append(node.right)
        
        if elements == max_current_level:
            print(current_level)
            current_level = []
            elements = 0
            max_current_level = next_level_elements
            next_level_elements = 0

INT_MAX = 1000
INT_MIN = -1000
def is_bst(node):
    return is_bst_helper(node, INT_MAX, INT_MIN)

def is_bst_helper(node, mini, maxi):
    if node is None:
        return True
    if node.value < mini or node.value > maxi:
        return False
    return is_bst_helper(node.left, mini, node.value - 1) and is_bst_helper(node.right, node.value + 1, maxi)

def isSymmetricHelper(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    else:
        return node1.value == node2.value and isSymmetricHelper(node1.left, node2.right) and isSymmetricHelper(node1.right, node2.left)

def isSymmetric(node):
    if node is None:
        return True
    return isSymmetricHelper(node.left, node.right)

# using stack data structure
def invertTree(node):
    if node is None:
        return None

    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    
    return node

def isSubtree(root, subRoot):
    if subRoot is None:
        return True
    if root is None:
        return False
    if root.value == subRoot.value:
        if is_same_tree(root.left, subRoot.left) and is_same_tree(root.right, subRoot.right):
            return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
