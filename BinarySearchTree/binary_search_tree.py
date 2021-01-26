# Heather Fryling
# 1/25/2021
# Binary Search Tree Implementation
# Based on class CS5800 Northeastern University Seattle by Zhifeng Sun

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

def swap_vals(node1, node2):
    temp = node1.val
    node1.val = node2.val
    node2.val = temp

def delete(root, val):
    # Base case = we found the value we want to delete.
    if root.val == val:
        # Case where the value to delete is in a leaf.
        if root.left == None and root.right == None:
            return None
        # Case where the value to delete is in a node with only a right child.
        if root.left == None:
            return root.right
        # Case where the value to delete is in a node with only a left child.
        if root.right == None:
            return root.left
        # Case where the value to delete is in a node with two children.
        pred = predecessor(root)
        # Swap to place the correct value in the node to preserve the BST
        # property after the deletion.
        swap_vals(pred, root)
        # Delete the value swapped to the end of the left subtree, where it
        # now resides in a leaf node.
        root.left = delete(root.left, val)
    # Searching for the correct node to delete.
    if val < root.val:
        root.left = delete(root.left, val)
    if val > root.val:
        root.right = delete(root.right, val)
    # This returns the root with the tree fixed. If the value wasn't found,
    # nothing is changed.
    return root

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

def inorder_recursive(bst):
    if bst == None:
        return
    inorder_recursive(bst.left)
    print(bst.val)
    inorder_recursive(bst.right)

# If this is done on a BST, the traversal will be in sorted order.
def inorder_iterative(bst):
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


