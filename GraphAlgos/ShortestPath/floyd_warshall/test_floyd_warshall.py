from floyd_warshall import *

def test_floyd_warshall():
    n1 = 5
    g1 = [[float('inf') for _ in range(n1)] for _ in range(n1)]
    for i in range(n1):
        g1[i][i] = 0
    g1[0][1] = 2
    g1[0][3] = -10
    g1[1][2] = -4
    g1[2][4] = 5
    g1[3][4] = -10
    dist1 = floyd_warshall(g1)
    ans1 = [[0, 2, -2, -10, -20],
            [float('inf'), 0, -4, float('inf'), 1],
            [float('inf'), float('inf'), 0, float('inf'), 5],
            [float('inf'), float('inf'), float('inf'), 0, -10],
            [float('inf'), float('inf'), float('inf'), float('inf'), 0]]
    assert(ans1 == dist1)

    n2 = 4
    g2 = [[float('inf') for _ in range(n2)] for _ in range(n2)]
    for i in range(n2):
        g2[i][i] = 0
    g2[0][1] = 2
    g2[1][2] = 1
    g2[1][3] = 3
    g2[2][0] = -1
    g2[3][2] = 1
    dist2 = floyd_warshall(g2)
    ans2 = [[0, 2, 3, 5],
            [0, 0, 1, 3],
            [-1, 1, 0, 4],
            [0, 2, 1, 0]]
    assert(ans2 == dist2)