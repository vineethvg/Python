# Given N X N matrix filled with 1, 0, 2, 3.
# Find whether there is a path possible from source to destination, traversing through blank cells only. You can traverse up, down, right, and left.


# =================================================================================
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, d):

        if s == d:
            return True

        # marking all vertices not visited
        visited = [False]*(len(self.graph) + 1)

        queue = []
        queue.append(s)

        visited[s] = True
        while(queue):

            s = queue.pop(0)

            for i in self.graph[s]:

                if i == d:
                    return True

                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False


def isSafe(i, j, matrix):
    if i >= 0 and i <= len(matrix) and j >= 0 and j <= len(matrix[0]):
        return True
    else:
        return False


def findPath(M):
    s, d = None, None  # source and destination
    N = len(M)
    g = Graph()

    k = 1  # Number of current vertex
    for i in range(N):
        for j in range(N):
            if (M[i][j] != 0):

                if (isSafe(i, j + 1, M)):
                    g.addEdge(k, k + 1)
                if (isSafe(i, j - 1, M)):
                    g.addEdge(k, k - 1)
                if (isSafe(i + 1, j, M)):
                    g.addEdge(k, k + N)
                if (isSafe(i - 1, j, M)):
                    g.addEdge(k, k - N)

            if (M[i][j] == 1):
                s = k

            if (M[i][j] == 2):
                d = k
            k += 1

    return g.BFS(s, d)


if __name__ == '__main__':
    M = [[0, 3, 0, 1], [3, 0, 3, 3], [2, 3, 3, 3], [0, 3, 3, 3]]
    if findPath(M):
        print("Yes")
    else:
        print("No")
