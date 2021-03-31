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
    # Adding the first vertex to the cut.
    u = 0
    cut[0] = True
    parent[0] = None
    dist[0] = 0
    cut_count = 1
    while(cut_count < n):
        smallest_weight = float('inf')
        smallest_v = None
        smallest_u = None
        for u in range(n):
            if cut[u]:
                for v in g[u]:
                    if cut[v] == False:
                        if weights[u][v] < smallest_weight:
                            smallest_weight = weights[u][v]
                            smallest_u = u
                            smallest_v = v
        dist[smallest_v] = smallest_weight
        parent[smallest_v] = smallest_u
        cut[smallest_v] = True
        cut_count += 1
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
#O(n) forcut, parent, and dist.
def prims_custom_g(g, weights):
    n = len(g.graph.keys())
    cut = set({})
    parent = {}
    dist = {}
    for u in g.graph.keys():
        dist[u] = float('inf')
    # Adding the first vertex to the cut.
    u = list(g.graph.keys())[0]
    cut.add(u)
    dist[u] = 0
    parent[u] = None
    while(len(cut) < n):
        smallest_weight = float('inf')
        smallest_v = None
        smallest_u = None
        for u in g.graph.keys():
            if u in cut:
                for v in g.graph.keys():
                    if v not in cut:
                        if get_weight(u, v, weights) < smallest_weight:
                            smallest_weight = get_weight(u, v, weights)
                            smallest_u = u
                            smallest_v = v
        dist[smallest_v] = smallest_weight
        parent[smallest_v] = smallest_u
        cut.add(smallest_v)
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
# O(n) -- for cut, parent, cheapest, and hd.
def prims_custom_efficient(g, weights):
    cut = set({})
    parent = {}
    cheapest = {}
    hd = heapdict()
    # Add an initial vertex to the cut set.
    u = list(g.graph.keys())[0]
    cut.add(u)
    parent[u] = None
    # Initialize the priority queue.
    # No need to add non-crossing edges, as they will be inserted once they
    # are crossing.
    for v in g.graph[u]:
        hd[v] = weights[(u, v)]
        cheapest[v] = u
    while hd:
        w = hd.popitem()[0]
        cut.add(w)
        parent[w] = cheapest[w]
        # Update the new crossing edges.
        for y in g.graph[w]:
            # Only look at crossing edges.
            if y not in cut:
                if weights[(y, w)] < hd[y]:
                    hd[y] = weights[(y, w)]
                    cheapest[y] = w
    return parent