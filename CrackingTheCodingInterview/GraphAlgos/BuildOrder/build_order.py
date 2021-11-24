# dependencies are actually directed edges.
# I need to remember toposort.

def toposort(edges):
    graph = adj_list_from_edges(edges)
    V = graph.keys()
    state = {}
    for u in V:
        state[u] = -1
    topo_sorted = []
    for u in V:
         if state[u] == -1:
            dfs_topo(u, graph, state, topo_sorted)
    topo_sorted.reverse()
    return topo_sorted

def dfs_topo(u, graph, state, topo_sorted):
    state[u] += 1 # mark visiting
    for v in graph[u]:
        if state[v] == 0:
            raise ValueError('Cycle detected. No valid topological sort.')
        if state[v] == -1:
            dfs_topo(v, graph, state, topo_sorted)
    topo_sorted.append(u)
    state[u] += 1

def adj_list_from_edges(edges):
    adj_list = {}
    for edge in edges:
        s = edge[0]
        u = edge[1] 
        if s not in adj_list.keys():
            adj_list[s] = []
        if u not in adj_list.keys():
            adj_list[u] = []
        adj_list[s].append(u)
    return adj_list

dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]
dependencies2 = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c'], ['d', 'a']]

print(adj_list_from_edges(dependencies))
print(toposort(dependencies))
# print(toposort(dependencies2))
