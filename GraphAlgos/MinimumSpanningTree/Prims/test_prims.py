from prims import *

def test_prims():
    g1 = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
    weights1 = [[0, 1, 2, 2],
                [1, 0, float('inf'), 4],
                [2, float('inf'), 0, 3],
                [2, 4, 3, 0]]
    ans1 = [None, 0, 0, 0]
    assert(ans1 == prims(g1, weights1))

    g2 = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
    weights2 = [[0, 1, 4, 3],
                [1, 0, float('inf'), 2],
                [4, float('inf'), 0, 5],
                [3, 2, 5, 0]]

    ans2 = [None, 0, 0, 1]
    assert(ans2 == prims(g2, weights2))

def test_prims_custom():
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

    ans1 = {1: None, 2: 1, 3: 1, 4: 1}
    assert(ans1 == prims_custom_g(g1_custom, weights1_custom))

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

    ans2 = {'a': None, 'b': 'a', 'd': 'b', 'c': 'a'}
    assert(ans2 == prims_custom_g(g2_custom, weights2_custom))

def test_prims_custom_efficient():
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

    ans1 = {1: None, 2: 1, 3: 1, 4: 1}
    assert(ans1 == prims_custom_efficient(g1_custom, weights1_custom))

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

    ans2 = {'a': None, 'b': 'a', 'd': 'b', 'c': 'a'}
    assert(ans2 == prims_custom_efficient(g2_custom, weights2_custom))

