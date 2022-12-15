# Weighted graph represnted with an adjacency matrix


def add_vertex(v):
    """Add a vertex to the set of vertices and the graph"""
    global graph
    global vertices
    global vertices_no

    if v in vertices:
        print(f"Vertex {v} add_vertex")
    else:
        vertices_no += 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)


def add_edge(v1, v2, e):
    """Add an edge between v1 and v2 with edge weight e"""
    global graph
    global vertices
    global vertices_no

    # Check if vertex v1 and v2 are valid and exists in the graph
    if v1 not in vertices:
        print(f"Vertex {v1} DNE")
    elif v2 not in vertices:
        print(f"Vertex {v2} DNE")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e
    # NOTE: Since this code is not restricted to a directed graph or an
    # undirected graph, an edge betweern v1 and v2 does not imply that an
    # edge exists between v2 and v1


def print_graph():
    """Prints the graph"""
    global graph
    global vertices_no

    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(
                    f"{vertices[i]} -> {vertices[j]}, Edge Weight: {graph[i][j]}")


# Store the vertices in the graph
vertices = []

# Stores the number of vertices in the graph
vertices_no = 0
graph = []

# Add vertices
add_vertex("A")
add_vertex("B")
add_vertex("C")
add_vertex("D")
add_vertex("E")

# Add the edges betwen the vertices by specifying the
# from and to vertex along with the edge weight
add_edge("A", "B", 2)
add_edge("E", "A", 4)
add_edge("D", "C", 6)
add_edge("A", "D", 1)
add_edge("B", "C", 8)
add_edge("E", "C", 7)

print_graph()
print("\nInternal Representation:\n", graph)


# Output:
# A -> B, Edge Weight: 2
# A -> D, Edge Weight: 1
# B -> C, Edge Weight: 8
# D -> C, Edge Weight: 6
# E -> A, Edge Weight: 4
# E -> C, Edge Weight: 7
#
# Internal Representation:
# [[0, 2, 0, 1, 0], [0, 0, 8, 0, 0], [0, 0, 0, 0, 0], [0, 0, 6, 0, 0], [4, 0, 7, 0, 0]]


# https://medium.com/analytics-vidhya/graphs-in-python-adjacency-matrix-d0726620e8d7


"""
X = Null

    A  B  C  D  E
——————————————————
A | X  2  X  1  X
B | X  X  8  X  X
C | X  X  X  X  X
D | X  X  6  X  X
E | 4  X  7  X  X


A -> A, 0
A -> B, 2
A -> C, 0
A -> D, 1
A -> E, 0
"""
