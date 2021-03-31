# Heather Fryling
# 3/30/2021

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

