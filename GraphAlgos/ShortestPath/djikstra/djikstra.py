# Heather Fryling
# 3/20/2021

from heapdict import heapdict
from digraph import DiGraph

# PURPOSE
# Given a directed graph with no negative edge weights, g, in adjacency list 
# format, the weights of its edges, and a starting vertex, s, return the 
# lengths of the shortest paths to each vertex from s.
# SIGNATURE
# djikstra :: DiGraph, Dictionary, Vertex => Dictionary
# TIME COMPLEXITY
# O(nmlogn) -- for each vertex, updates the priority queue.
# SPACE COMPLEXITY
# O(n) -- for visited, heapdict, and distance.
def djikstra(g, weights, s):
    # Using a heapdict as a priority queue.
    hd = heapdict()
    visited = set({})
    distance = {}
    # Initializing the distances and heapdict to infinity.
    for u in g.graph.keys():
        hd[u] = float('inf')
        distance[u] = float('inf')
    # The distance to the starting point is 0.
    hd[s] = 0
    distance[s] = 0
    # Visit each node once when it is at the top of the priority queue.
    while(len(visited) < len(g.graph.keys())):
        u = hd.popitem()[0]
        visited.add(u)
        for v in g.graph[u]:
            if distance[u] + weights[(u, v)] < distance[v]:
                distance[v] = distance[u] + weights[(u, v)]
                # Update the priority of the node according to its 
                # new distance.
                hd[v] = distance[u] + weights[(u, v)]
    return distance