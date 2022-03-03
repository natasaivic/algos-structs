from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for i in range(vertices):
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    # Directed graph, (1,0) is not equal to (0,1)
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].insert_at_head(destination)    
            # Undirected graph       
            # self.array[destination].insert_at_head(source)

    def print_graph(self):
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            current = self.array[i].get_head()
            while current is not None:
                print("[", current.value, end=" ] -> ")
                current = current.next
            print("None")
