# Heather Fryling
# 3/8/2021

from digraph import *
from collections import deque

# PURPOSE
# Use bfs to find the shortest path from start vertex to every other
# vertex in the graph, g.
# This function returns the length of the shortest paths in distances and
# the immediate predecessor of each node in the parent dictionary.
# The parent dictionary can be used to reconstruct the shortest path to
# any vertex from the start.
# SIGNATURE
# bfs_shortest_path :: Digraph, Integer => Tuple(Dictionary, Dictionary)
# TIME COMPLEXITY
# O(m) -- bfs checks each edge once.
# SPACE COMPLEXITY
# O(n) -- each dictionary contains an entry for each vertex.
def bfs_shortest_path(g, start):
    q = deque()
    q.append(start)
    visited = set({})
    visited.add(start)
    parent = {}
    distances = {}
    distances[start] = 0
    while(q):
        curr = q.popleft()
        for neighbor in g.graph[curr]:
            if neighbor not in visited:
                parent[neighbor] = curr
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[curr] + 1
    return (distances, parent)