# =========================Graph Opertaions ===================================

# take two empty lists
from os import close


nodes = []
graph = []
node_count = 0  # if u wanna count node count


# INSERTION OPERATION///////////////////////

# FUNCTION TO ADD NODE---------------------------------------------------------------
# adding a node(matrix representation)

def add_node(v):

    global node_count
    if v in nodes:
        print("The node is already present")

    # if the node is not present in the graph,
    # then u have to append the node a.k.a v to the nodes list.
    # node_count will count the number of nodes being added
    else:
        node_count = node_count + 1
        nodes.append(v)

        # whenever u are adding a node to the graph, that means
        # you are creating a row and a column in the adjacency matrix.
        # so if there is no edge between the existing nodes and your
        # new node, then its gonna be represented as 0 in the matrix.

        # Since we are just adding nodes and not edges, obviously its
        # gonna be 0 in the matrix

        # This loop will add zero to the new node column
        #                           Example :    A  B   C   D   new_node
        for n in graph:             # A         [0  1   0   0   n.append(0)]
            n.append(0)             # B         [1  0   0   0   n.append(0)]
        #                           # C         [0  0   1   1   n.append(0)]
        #                           # D         [1  0   1   1   n.append(0)]

        # This loop will create a list of zeros and append it to the graph as
        # a new row
        #                               Example:   A    B   C   D   new_node
        temp = []                       # A       [0    1   0   0   0   ]
        for i in range(node_count):     # B       [1    0   0   0   0   ]
            temp.append(0)              # C       [0    0   1   1   0   ]
        graph.append(temp)              # D       [1    0   1   1   0   ]
        #                               # temp    [0    0   0   0   0   ]

# FUNCTION TO ADD EDGE-------------------------------------------------------------------
# adding edge(matrix representation)

# graphs has:
# 1) unweighted undirected type (no cost/weight on edges, and no direction for edges)
# 2) weighted undirected type   (has cost/weight on edges, and no direction for edges)
# 3) unweighted directed type   (no cost/weight on edges, but direction for edges)
# 4) weighted directed type     (has cost/weight on edges, and direction for edges)


def add_edge(v1, v2, cost):  # if you want dont want to consider weight or cost, remove cost
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost

        # if the graph is directed, then dont consider this below line
        graph[index2][index1] = cost

        # and and and!!! if the graph has no cost, then u have to set,
        # graph[index1][index2] = 1
        # graph[index2][index1] = 1


# DELETION OPERATION///////////////////////

# FUNCTION TO DELETE NODE -------------------------------------------------------
# deleting node (matrix representation)

def del_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in graph")
    else:

        # first find the index of node that u wanna delete
        # then decrement node_count
        # remove node
        # then remove row of the matrix
        # and remove the column of matrix

        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

# FUNCTION TO DELETE EDGE -------------------------------------------------------
# deleting edge(matrix representation)


def del_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in graph")
    elif v2 not in nodes:
        print(v2, "is not present in graph")
    else:

        # the logic is same as in adding edges, instead of making 1,
        # we are deleting edge by making it zero.

        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0

        # if the graph is directed, then dont consider this below line
        graph[index2][index1] = 0


# FUNCTION TO PRINT GRAPH --------------------------------------------------------

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


# DRIVER CODE---------------------------------------------------------------------
# add nodes
add_node("A")
add_node("B")
add_node("C")
add_node("D")

# add edges
add_edge("A", "B", 10)
add_edge("A", "D", 5)

print("graph before deleting")
print(graph)
print_graph()

print()


# delete nodes
del_node("D")

# delete edges
del_edge("A", "B")

print("graph after deleting")
print(graph)
print_graph()
