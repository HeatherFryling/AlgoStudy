# Given a binary search tree,
# return all possible arrays that
# could form the bst.

# Invariant:
# Parents must always be added
# before children.

# Idea: Generate all permutations
# but the only node available for
# each permutation are children
# whose parents have already been added.

# Time Complexity:
# Depth: logn
# Branching Factor: n
# Work per call: n
# O(n^nlogn)

# Space Complexity:
# O(n!)

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node[{}, {}, {}]".format(self.val, self.left, self.right)

def all_bst_orders(root):
    res = []
    available = set([root])
    path = []
    helper(available, path, res)
    return res

def helper(available, path, res):
    if not available:
        cp = path.copy()
        res.append(cp)
        return
    avail = list(available)
    for node in avail:
        available.remove(node)
        if node.left:
            available.add(node.left)
        if node.right:
            available.add(node.right)
        path.append(node.val)

        helper(available, path, res)

        path.pop()
        if node.left:
            available.remove(node.left)
        if node.right:
            available.remove(node.right)
        available.add(node)

tree1 = Node(2)
tree1.left = Node(1)
tree1.right = Node(3)

tree2 = Node(3)
tree2.left = Node(1)
tree2.right = Node(5)
tree2.right.left = Node(4)
tree2.right.right = Node(6)

print(all_bst_orders(tree1))

print(all_bst_orders(tree2))