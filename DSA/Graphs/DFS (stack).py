# recursion approach

# unweighted and undirected graph
def add_node(v):
    if v in graph:
        print("The node is already present")
    else:
        graph[v] = []


def add_edge(v1, v2):  # if you want dont want to consider weight or cost, remove cost
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def DFS(node, visited, graph):
    if node not in graph:
        print("Node is missing!")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)


visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

# add edges
add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")
add_edge("C", "D")
add_edge("E", "D")
print(graph)
DFS("B", visited, graph)
