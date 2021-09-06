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
