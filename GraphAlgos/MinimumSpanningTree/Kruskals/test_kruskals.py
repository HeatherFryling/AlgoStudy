from kruskals import *

def test_kruskals_custom():
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

    ans1 = {(1, 2), (1, 3), (1, 4)}
    assert(ans1 == kruskals(g1_custom, weights1_custom))

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

    ans2 = {('a','b'), ('b', 'd'), ('a', 'c')}
    assert(ans2 == kruskals(g2_custom, weights2_custom))