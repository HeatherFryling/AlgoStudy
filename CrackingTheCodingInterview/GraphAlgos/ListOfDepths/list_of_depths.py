from collections import deque
from bst_node import BST_Node

# O(E + V) time | O(V) space
def list_of_depths(BST):
    depths = []
    if BST == None:
        return depths
    q = deque()
    curr = BST
    q.append(curr)

    while(len(q) > 0):
        level_size = len(q)
        level = []
        while len(level) < level_size:
            curr = q.popleft()
            level.append(curr.value)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        depths.append(level)

    return depths

test1 = None

test2 = BST_Node(1)

test3 = BST_Node(1)
test3.left = BST_Node(2)
test3.right = BST_Node(3)

test4 = BST_Node(1)
test4.left = BST_Node(2)
test4.right = BST_Node(3)
test4.left.left = BST_Node(4)
test4.left.right = BST_Node(5)
test4.right.right = BST_Node(6)
test4.right.left = BST_Node(7)

test5 = BST_Node(1)
test5.right = BST_Node(2)
test5.right.right = BST_Node(3)
test5.right.right.right = BST_Node(4)

test6 = BST_Node(1)
test6.left = BST_Node(2)
test6.left.right = BST_Node(3)
test6.right = BST_Node(4)
test6.right.left = BST_Node(6)
test6.right.left.right = BST_Node(7)
test6.right.right = BST_Node(5)

tests = [test1, test2, test3, test4, test5, test6]

for test in tests:
    print(list_of_depths(test))

