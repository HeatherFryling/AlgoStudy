# Heather Fryling
# 3/31/2021

# This is a quick and dirty implementation of UnionFind for use in optimized
# Kruskal's algorithm.

class UnionFind:

    parent = {}
    rank = {}

    # PURPOSE
    # Construct a UnionFind object from a list of items. Each item begins
    # as its own disjoint set.
    # SIGNATURE
    # __init__ :: Self, List => UnionFind
    def __init__(self, items):
        for item in items:
            self.parent[item] = item
            self.rank[item] = 0

    # PURPOSE
    # Find and return the set in which an item is stored. Update item's parent
    # to the root (path compression).
    # SIGNATURE
    # find :: Self, Item => Item
    # TIME COMPLEXITY
    # O(log*n)
    # SPACE COMPLEXITY
    # O(1)
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    # PURPOSE
    # Given two roots, that is the labels of disjoint sets, (items farther
    # down the tree cannot be passed as parameters in this implementation
    # of union), join the two sets. Update the rank of the new root. Updated
    # rank will be accurate once path compression is accomplished.
    # SIGNATURE
    # union :: Self, Item, Item => None
    # TIME COMPLEXITY
    # O(1)
    # SPACE COMPLEXITY
    # O(1)
    def union(self, root1, root2):
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root2] < self.rank[root1]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

    # PURPOSE
    # Given this UnionFind and another object, compare them for equality and
    # return the result. Objects are considered equal if both are of type
    # UnionFind and their parent and rank dictionaries are the same.
    # There is a possibility of error here, as the same sets may look different
    # before and after path compression, but fixing that is beyond the scope
    # of this quick and dirty implementation.
    # SIGNATURE
    # __eq__ :: Self, Object => Boolean
    def __eq__(self, other):
        if type(other) != UnionFind:
            return False
        return self.parent == other.parent and self.rank == other.rank

    # PURPOSE
    # Return a String representation of this UnionFind object.
    # SIGNATURE
    # __repr__ :: Self => String
    def __repr__(self):
        return "UnionFind{parent=" \
                + str(self.parent) \
                + ", rank=" \
                + str(self.rank) \
                + "}"