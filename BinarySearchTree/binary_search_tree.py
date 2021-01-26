# Heather Fryling
# 1/25/2021
# Binary Search Tree Implementation

# Required methods:
#    insert(k, n)
#    get(k)
#    delete(k)

# Traversals
# Pre-Order
# Post-Order
# In-Order
# Level-Order

from collections import deque

class TreeNode:

    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# PURPOSE
# Inset a value into the binary search tree rooted at root.
# SIGNATURE
# insert :: TreeNode, Integer => TreeNode
# TIME COMPLEXITY
# O(h)
# SPACE COMPLEXITY
# O(h) calls on the stack
def insert(root, val):
    if root == None:
        return TreeNode(val)
    if root.val < val:
        root.right = insert(root.right, val)
    if root.val > val:
        root.left = insert(root.left, val)
    return root

def predecessor(node):
    curr = node.left
    while curr.right != None:
        curr = curr.right
    return curr

def successor(node):
    curr = node.right
    while curr.left != None:
        curr = curr.left
    return curr

def delete(root, val):
    # Base case = we found the value we want to delete.
    if root.val == val:
        if node.left == None and node.right == None:
        return None
        if node.left == None:
        return node.right
        if node.right == None:
            return node.left
        pred = predecessor(node)
        swap(pred, node)


    pass

def preorder_recursive(bst):
    if (bst == None):
        return
    print(bst.val)
    preorder_recursive(bst.left)
    preorder_recursive(bst.right)

def preorder_iterative(bst):
    if (bst == None):
        return []
    stack = deque()
    traversal = []
    stack.append(bst)
    while stack:
        curr = stack.pop()
        traversal.append(curr.val)
        if curr.right != None:
            stack.append(curr.right)
        if curr.left != None:
            stack.append(curr.left)
    return traversal

# If this is done on a BST, the traversal will be in sorted order.
def inorder_recursive(bst):
    if bst == None:
        return []
    stack = deque()
    traversal = []
    curr = bst
    while curr != None or stack:
        # Push the left subtree onto the stack.
        while curr != None:
            stack.append(curr)
            curr = curr.left
        # Pop off the leftmost node and get its value.
        curr = stack.pop()
        traversal.append(curr.val)
        # Explore the right subtree
        curr = curr.right
    return traversal

seven = TreeNode(7)
test_tree = seven
five = TreeNode(5)
test_tree.left = five
eleven = TreeNode(11)
test_tree.right = eleven
two = TreeNode(2)
test_tree.left.left = two
six = TreeNode(6)
test_tree.left.right = six
one = TreeNode(1)
test_tree.left.left.left = one
three = TreeNode(3)
test_tree.left.left.right = three
twelve = TreeNode(12)
test_tree.right.right = twelve


