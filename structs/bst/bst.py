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
    