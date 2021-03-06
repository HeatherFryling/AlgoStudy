from basic_bfs import *

def test_bfs():
    g = DiGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 3)
    assert([1, 2, 3, 4] == bfs(g, 1, set({}), []))

def test_bfs_all():
    g = DiGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 3)
    g.add_vertex(5)
    assert([1, 2, 3, 4, 5] == bfs_all(g))