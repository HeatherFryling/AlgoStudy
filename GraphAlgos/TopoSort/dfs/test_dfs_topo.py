from dfs_topo import *

def test_dfs_topo():
    g = DiGraph()
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    assert([2, 3, 1, 4, 5] == dfs_topo_all(g))