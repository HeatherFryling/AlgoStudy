from bfs_shortest_path import *

def test_bfs_shortest_path():
    g = DiGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    data = bfs_shortest_path(g, 1)
    assert({1: 0, 2: 1, 3: 1, 4: 2, 5: 3} == data[0])
    assert({2: 1, 3: 1, 4: 3, 5: 4} == data[1])