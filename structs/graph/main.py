from Graph import Graph
from Queue import MyQueue
from Stack import MyStack

g = Graph(4)
g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()

print(g.array[0].get_head().value)
print(g.array[1].get_head().value)
print(g.array[2].get_head().value)

def bfs_traversal_helper(g, source, visited):
    result = ""
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True # Mark as visited
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head
        while temp is not None:
            if not visited[temp.value]:
                queue.enqueue(temp.value)
                visited[temp.value] = True  # Visit the current Node
            temp = temp.next
    return result, visited

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result

def dfs_traversal_helper(g, source, visited):
    result = ""
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    while not stack.is_empty():
        current_node = stack.pop()
        result += str(current_node)
        temp = g.array[current_node].head
        while temp is not None:
            if not visited[temp.value]:
                stack.push(temp.value)
                visited[temp.value] = True
            temp = temp.next
    return result, visited  

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    result, visited = dfs_traversal_helper(g, source, visited)
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


if __name__ == "__main__" :
    g = Graph(4)
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(bfs_traversal(g, 0))

    g2 = Graph(7)
    num_of_vertices = g2.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g2.add_edge(1, 2)
        g2.add_edge(1, 3)
        g2.add_edge(2, 4)
        g2.add_edge(2, 5)
        g2.add_edge(3, 6)
        print(dfs_traversal(g2, 1))