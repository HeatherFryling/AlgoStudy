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
    count = 1

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1

    def __str__(self):
        l = "None" if self.left == None else self.left.val
        r = "None" if self.right == None else self.right.val
        return "NODE[val: {val}, left: {left}, right: {right}, count: {count}]"\
            .format(val = self.val, left = l, right = r, count = self.count)

    def __repr__(self):
        return str(self.val)

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
    root.count = 1
    if root.val < val:
        root.right = insert(root.right, val)
    if root.val > val:
        root.left = insert(root.left, val)
    if root.left != None:
        root.count += root.left.count
    if root.right != None:
        root.count += root.right.count
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
            root.count -= 1
            return None
        # Case where the value to delete is in a node with only a right child.
        if root.left == None:
            root.count -= 1
            return root.right
        # Case where the value to delete is in a node with only a left child.
        if root.right == None:
            root.count -= 1
            return root.left
        # Case where the value to delete is in a node with two children.
        pred = predecessor(root)
        # Swap to place the correct value in the node to preserve the BST
        # property after the deletion.
        swap_vals(pred, root)
        # Delete the value swapped to the end of the left subtree, where it
        # now resides in a leaf node.
        root.left = delete(root.left, val)
        root.count = 1
        if root.left != None:
            root.count += root.left.count
        if root.right != None:
            root.count += root.right.count
        return root
    # Searching for the correct node to delete.
    if val < root.val:
        root.left = delete(root.left, val)
    if val > root.val:
        root.right = delete(root.right, val)
    # This returns the root with the tree fixed. If the value wasn't found,
    # nothing is changed.
    root.count = 1
    if root.left != None:
        root.count += root.left.count
    if root.right != None:
        root.count += root.right.count
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

def inorder_rec(bst):
    return inorder_recursive(bst, [])

def inorder_recursive(bst, traversal):
    if bst == None:
        return traversal
    inorder_recursive(bst.left, traversal)
    traversal.append(bst.val)
    inorder_recursive(bst.right, traversal)
    return traversal

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

def reconstruct_bst_preorder(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    stack = deque()
    stack.append(root)
    for i in range(1, len(arr)):
        parent = stack[-1]
        child = TreeNode(arr[i])
        curr_num = arr[i]
        # First move up the stack until you find the parent of the value you're
        # examining.
        while stack and stack[-1].val < curr_num:
            parent = stack.pop()

        # If we made it to the end of the stack and still didn't find a value
        # greater than the child, it's a right child
        if parent.val < child.val:
            parent.right = child
        # Otherwise, this is the left child.
        else:
            parent.left = child
        # The child is now a potential parent for the rest of the values in the
        # array.
        stack.append(child)
    return root

def validate_bst(root):
    return is_bst(root, None, None)

def is_bst(root, low, high):
    if root == None:
        return True
    val = root.val
    if low != None and val <= low:
        return False
    if high != None and val >= high:
        return False
    if not (is_bst(root.right, val, high)):
        return False
    if not (is_bst(root.left, low, val)):
        return False
    return True

def kth_largest(bst, k):
    rank = bst.count
    if bst.right != None:
        rank = rank - bst.right.count
    if k == rank:
        return bst.val
    if k < rank:
        return kth_largest(bst.left, k)
    if k > rank:
        return kth_largest(bst.right, k - rank)
    return rank


# seven = TreeNode(7)
# test_tree = seven
# five = TreeNode(5)
# test_tree.left = five
# eleven = TreeNode(11)
# test_tree.right = eleven
# two = TreeNode(2)
# test_tree.left.left = two
# six = TreeNode(6)
# test_tree.left.right = six
# one = TreeNode(1)
# test_tree.left.left.left = one
# three = TreeNode(3)
# test_tree.left.left.right = three
# twelve = TreeNode(12)
# test_tree.right.right = twelve
# in_order = [1, 2, 3, 5, 6, 7, 11, 12]

# print(inorder_rec(test_tree))

seven = TreeNode(7)
insert(seven, 5)
insert(seven, 11)
insert(seven, 2)
insert(seven, 12)
insert(seven, 6)
insert(seven, 3)
insert(seven, 1)
insert(seven, 10)
print(preorder_iterative(seven))
traversal = [7, 5, 2, 1, 3, 6, 11, 10, 12]
print(reconstruct_bst_preorder(traversal))




