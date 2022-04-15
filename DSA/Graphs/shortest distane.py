from collections import defaultdict
from queue import PriorityQueue


def shortest(graph, start_vertex, end_vertex):

    visited = []

    D = {v: float('inf') for v in range(len(graph))}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in range(len(graph)):
            if graph[current_vertex][neighbor] != -1:
                distance = graph[current_vertex][neighbor]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D[end_vertex]


n, m = list(map(int, input().strip().split(' ')))

graph = [[-1 for i in range(n)] for j in range(n)]

for _ in range(m):
    src, dest = list(map(int, input().strip().split()))
    graph[src][dest] = 1

start, end = list(map(int, input().strip().split()))
print(shortest(graph, start, end))
