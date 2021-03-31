# Heather Fryling
# 3/30/2021

from graph import Graph

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
    return(dist, parent)

def get_weight(u, v, weights):
    if u == v:
        return 0
    if (u, v) in weights.keys():
        return weights[(u, v)]
    return float('inf')

def prims_custom_g(g, weights):
    n = len(g.graph.keys())
    cut = set({})
    parent = {}
    for u in g.graph.keys():
        parent[u] = None
    dist = {}
    for u in g.graph.keys():
        dist[u] = float('inf')
    # Adding the first vertex to the cut.
    u = list(g.graph.keys())[0]
    cut.add(u)
    dist[u] = 0
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
    return(dist, parent)

g1 = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
weights1 = [[0, 1, 2, 2],
            [1, 0, float('inf'), 4],
            [2, float('inf'), 0, 3],
            [2, 4, 3, 0]]

print(prims(g1, weights1))

g2 = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
weights2 = [[0, 1, 4, 3],
            [1, 0, float('inf'), 2],
            [4, float('inf'), 0, 5],
            [3, 2, 5, 0]]

print(prims(g2, weights2))

g1_custom = Graph()
g1_custom.add_edge(1, 2)
g1_custom.add_edge(1, 3)
g1_custom.add_edge(1, 4)
g1_custom.add_edge(2, 4)
g1_custom.add_edge(3, 4)

weights1_custom = {}
weights1_custom[(1, 2)] = 1
weights1_custom[(2, 1)] = 1
weights1_custom[(1, 3)] = 2
weights1_custom[(3, 1)] = 2
weights1_custom[(1, 4)] = 2
weights1_custom[(4, 1)] = 2
weights1_custom[(2, 4)] = 4
weights1_custom[(4, 2)] = 4
weights1_custom[(3, 4)] = 3
weights1_custom[(4, 3)] = 3

print(prims_custom_g(g1_custom, weights1_custom))

g2_custom = Graph()
g2_custom.add_edge('a', 'b')
g2_custom.add_edge('a', 'c')
g2_custom.add_edge('a', 'd')
g2_custom.add_edge('b', 'd')
g2_custom.add_edge('c', 'd')

weights2_custom = {}
weights2_custom[('a', 'b')] = 1
weights2_custom[('b', 'a')] = 1
weights2_custom[('a', 'c')] = 4
weights2_custom[('c', 'a')] = 4
weights2_custom[('a', 'd')] = 3
weights2_custom[('d', 'a')] = 3
weights2_custom[('b', 'd')] = 2
weights2_custom[('d', 'b')] = 2
weights2_custom[('c', 'd')] = 5
weights2_custom[('d', 'c')] = 5

print(prims_custom_g(g2_custom, weights2_custom))
