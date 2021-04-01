from union_find import UnionFind

def test_init():
    items = [1, 2, 3, 4]
    test = UnionFind(items)
    test_parent = {1: 1, 2: 2, 3: 3, 4: 4}
    test_rank = {1: 0, 2: 0, 3: 0, 4: 0}

    assert(test_parent == test.parent)
    assert(test_rank == test.rank)

def test_union():
    items = [1, 2, 3, 4]
    test = UnionFind(items)
    test.union(1, 2)
    test_parent = {1: 1, 2: 1, 3: 3, 4: 4}
    test_rank = {1: 1, 2: 0, 3: 0, 4: 0}
    assert(test_parent == test.parent)
    assert(test_rank == test.rank)
    test.union(2, 3)
    parent2 = {1: 1, 2: 1, 3: 2, 4: 4}
    rank2 = {1: 1, 2: 1, 3: 0, 4: 0}
    assert(parent2 == test.parent)
    assert(rank2 == test.rank)

def test_find():
    items = [1, 2, 3, 4]
    test = UnionFind(items)
    for item in items:
        assert(test.find(item) == item)
    test.union(1, 2)
    assert(test.find(1) == 1)
    assert(test.find(2) == 1)
    assert(test.find(3) == 3)
    assert(test.find(4) == 4)
    test.union(2, 3)
    test.union(3, 4)
    uncompressed = {1: 1, 2: 1, 3: 2, 4: 3}
    assert(uncompressed == test.parent)
    test.find(4)
    compressed = {1: 1, 2: 1, 3: 1, 4: 1}
    assert(compressed == test.parent)