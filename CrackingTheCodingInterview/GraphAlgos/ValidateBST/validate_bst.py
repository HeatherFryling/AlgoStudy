from bst_node import BST_Node

# Oz(n) time | O(height) space
def validate_bst(BST):
    left_valid = validate_bst_helper(BST.left, float('-inf'), BST.value)
    right_valid = validate_bst_helper(BST.right, BST.value + 1, float('inf'))
    return left_valid and right_valid

def validate_bst_helper(BST, smallest, largest):
    if BST == None:
        return True

    if BST.value < smallest:
        return False

    if BST.value > largest:
        return False

    left_valid = validate_bst_helper(BST.left, smallest, BST.value)
    right_valid = validate_bst_helper(BST.right, BST.value + 1, largest) 

    return left_valid and right_valid

# Balanced
test1 = BST_Node(5)
test1.left = BST_Node(3)
test1.right = BST_Node(7)
test1.left.right = BST_Node(4)
test1.left.left = BST_Node(2)
test1.right.left = BST_Node(6)
test1.right.right = BST_Node(8)

print(validate_bst(test1))

# Unbalanced
test2 = BST_Node(5)
test2.left = BST_Node(3)
test2.right = BST_Node(7)
test2.left.right = BST_Node(4)
test2.left.left = BST_Node(2)
test2.right.left = BST_Node(4)
test2.right.right = BST_Node(8)

print(validate_bst(test2))