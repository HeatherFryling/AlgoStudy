from bfs_cc import *

def test_bfs_cc():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_vertex(4)
    g.add_edge(5, 6)
    assert({1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 3} == bfs_cc_all(g))