# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

from collections import defaultdict, deque


def sol(routes, source, target):
    stops = defaultdict(list)
    for bus, route in enumerate(routes):
        for stop in route:
            stops[stop].append(bus)

    if source not in stops or target not in stops:
        return -1

    q = deque([source])
    visited = set([source])
    busCounts = 0
    while q:
        sameLevelCounts = len(q)
        for _ in range(sameLevelCounts):
            current = q.popleft()
            if current == target:
                return busCounts
            for bus in stops[current]:
                for stop in routes[bus]:
                    if stop not in visited:
                        visited.add(stop)
                        q.append(stop)
                routes[bus] = []  # set visited route to empty
        busCounts += 1
    return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
print(sol(routes, source, target))
