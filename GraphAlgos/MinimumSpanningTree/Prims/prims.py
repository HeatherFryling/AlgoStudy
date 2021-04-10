# Heather Fryling
# 3/30/2021

from graph import Graph
from heapdict import heapdict

# PURPOSE
# Given an undirected, connected graph, return the edges that comprise its
# minimum spanning tree.
# SIGNATURE
# prims :: Graph, Dictionary => Dictionary
# TIME COMPLEXITY
# O(n^2)
# SPACE COMPLEXITY
# O(n) for cut, parent, dist
def prims(g, weights):
    n = len(g)
    cut = [False for u in range(n)]
    parent = [None for u in range(n)]
    dist = [float('inf') for u in range(n)]
    parent[0] = None
    dist[0] = 0
    cut_count = 0
    while(cut_count < n):
        smallest_dist = float('inf')
        smallest_u = None
        # Inefficiently finding the smallest distance by iterating over the
        # whole list of vertices.
        for u in range(n):
            if not cut[u]:
                if dist[u] < smallest_dist:
                    smallest_u = u
                    smallest_dist = dist[u]
        # Pulling the minimum into the already processed set.
        cut[smallest_u] = True
        cut_count += 1
        # Updating distances with the new crossing edges.
        for v in g[smallest_u]:
            if weights[smallest_u][v] < dist[v]:
                dist[v] = weights[smallest_u][v]
                parent[v] = smallest_u
    return parent

# PURPOSE
# Helper function to get the weight of an edge given u, v, and a weights
# dictionary with (u, v) edges as keys.
# SIGNATURE
# get_weight :: Vertex, Vertex, Dictionary => Float
# TIME COMPLEXITY
# O(1)
# SPACE COMPLEXITY
# O(1)
def get_weight(u, v, weights):
    if u == v:
        return 0
    if (u, v) in weights.keys():
        return weights[(u, v)]
    return float('inf')

# PURPOSE
# Given an undirected, connected graph, return the edges that comprise its
# minimum spanning tree. This time, instead of using lists, use a dictionary-
# based custom implementation of a graph adjacency list data structure to
# allow more flexibility in naming of vertices.
# SIGNATURE
# prims_custom :: Graph, Dictionary => Dictionary
# TIME COMPLEXITY
# O(n^2)
# SPACE COMPLEXITY
#O(n) for cut, parent, and dist.
def prims_custom_g(g, weights):
    n = len(g.graph.keys())
    cut = set({})
    parent = {}
    dist = {}
    for u in g.graph.keys():
        dist[u] = float('inf')
    u = list(g.graph.keys())[0]
    dist[u] = 0
    parent[u] = None
    while(len(cut) < n):
        smallest_dist = float('inf')
        smallest_u = None
        # Get the vertex with the smallest distance to the cut.
        for u in g.graph.keys():
            if u not in cut:
                if dist[u] < smallest_dist:
                    smallest_u = u
                    smallest_dist = dist[u]
        # Add the smallest distance vertex to the cut set.
        cut.add(smallest_u)
        # Update distances to the cut
        for v in g.graph[smallest_u]:
            if v not in cut and get_weight(smallest_u, v, weights) < dist[v]:
                dist[v] = get_weight(smallest_u, v, weights)
                parent[v] = smallest_u
    return parent

# PURPOSE
# Given an undirected, connected graph, return the edges that comprise its
# minimum spanning tree. This time use the custom graph data structure as
# well as a priority queue. The priority queue speeds up getting the minimum
# crossing edge.
# SIGNATURE
# prims_custom_efficient :: Graph, Dictionary => Dictionary
# TIME COMPLEXITY
# O((n + m)logn) -- All vertices and up to all edges are processed through the 
# priority queue.
# SPACE COMPLEXItY
# O(n) -- for cut, parent, dist, and hd.
def prims_custom_efficient(g, weights):
    cut = set({})
    parent = {}
    dist = {}
    hd = heapdict()
    for u in g.graph.keys():
        dist[u] = float('inf')
    u = list(g.graph.keys())[0]
    dist[u] = 0
    parent[u] = None
    hd[u] = 0
    while hd:
        smallest_u = hd.popitem()[0]
        cut.add(smallest_u)
        # Update the new crossing edges.
        for v in g.graph[smallest_u]:
            if v not in cut and get_weight(smallest_u, v, weights) < dist[v]:
                dist[v] = get_weight(smallest_u, v, weights)
                hd[v] = get_weight(smallest_u, v, weights)
                parent[v] = smallest_u
    return parent