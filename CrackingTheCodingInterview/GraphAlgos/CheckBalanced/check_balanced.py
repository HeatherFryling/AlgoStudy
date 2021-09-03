from bst_node import BST_Node

class TreeInfo:
    def __init__(self, height_left, height_right, is_balanced):
        self.height_left = height_left
        self.height_right = height_right
        self.is_balanced = is_balanced
    
    def get_height(self):
        return max(self.height_left, self.height_right)

def check_balanced(BST):
    tree_info = dfs_balanced(BST)
    return tree_info.is_balanced

def dfs_balanced(BST):
    if BST == None:
        return TreeInfo(0, 0, True)

    left_info = dfs_balanced(BST.left)
    right_info = dfs_balanced(BST.right)

    balanced_top = abs((left_info.get_height()) - (right_info.get_height())) <= 1

    balanced_tree = left_info.is_balanced and right_info.is_balanced and balanced_top
    return TreeInfo(left_info.get_height() + 1, right_info.get_height() + 1, balanced_tree)

# True
test1 = None

# True
test2 = BST_Node(1)

# True
test3 = BST_Node(1)
test3.left = BST_Node(2)
test3.right = BST_Node(3)

# True
test4 = BST_Node(1)
test4.left = BST_Node(2)
test4.right = BST_Node(3)
test4.left.left = BST_Node(4)
test4.left.right = BST_Node(5)
test4.right.right = BST_Node(6)
test4.right.left = BST_Node(7)

# False
test5 = BST_Node(1)
test5.right = BST_Node(2)
test5.right.left= BST_Node(3)

# True
test6 = BST_Node(1)
test6.left = BST_Node(2)
test6.left.right = BST_Node(3)
test6.right = BST_Node(4)
test6.right.left = BST_Node(6)
test6.right.left.right = BST_Node(7)
test6.right.right = BST_Node(5)

# False
test7 = BST_Node(1)
test7.left = BST_Node(2)
test7.left.right = BST_Node(3)
test7.right = BST_Node(4)
test7.right.left = BST_Node(6)
test7.right.left.right = BST_Node(7)
test7.right.left.right.right = BST_Node(8)
test7.right.right = BST_Node(5)

tests = [test1, test2, test3, test4, test5, test6, test7]

for test in tests:
    print(check_balanced(test))