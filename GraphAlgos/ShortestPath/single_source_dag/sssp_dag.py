# Heather Fryling
# 3/19/2020

from collections import deque
from digraph import DiGraph

def calc_in_degree(g):
    in_degree = {}
    for u in g.graph.keys():
        in_degree[u] = 0
    for u in g.graph.keys():
        for v in g.graph[u]:
            in_degree[v] += 1
    return in_degree

def bfs_topo(g):
    q = deque()
    topo = []
    in_degree = calc_in_degree(g)
    for u in in_degree.keys():
        if in_degree[u] == 0:
            q.append(u)
    while(q):
        u = q.popleft()
        topo.append(u)
        for v in g.graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    return topo

def relax(u, v, dist, cost):
    if (u, v) not in cost:
        return
    if dist[u] + cost[(u, v)] < dist[v]:
        dist[v] = dist[u] + cost[(u, v)]

def sssp_dag(g, s, cost):
    topo_order = bfs_topo(g)
    dist = {}
    for u in g.graph.keys():
        dist[u] = float('inf')
    dist[s] = 0
    # Check each edge to see if it might offer a shorter path.
    for u in topo_order:
        for v in g.graph[u]:
            relax(u, v, dist, cost)
    return dist

g = DiGraph()
g.add_edge(4, 2)
g.add_edge(4, 1)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 5)
g.add_edge(1, 5)
cost = {}
cost[(4, 2)] = 1
cost[(4, 1)] = 3
cost[(1, 3)] = 1
cost[(2, 3)] = 2
cost[(3, 5)] = 4
cost[(1, 5)] = 3

print(calc_in_degree(g))
print(bfs_topo(g))
print(sssp_dag(g, 2, cost))