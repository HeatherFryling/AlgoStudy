from bst_node_parent import BST_Node_Parent_Included

def successor(tree):
    if tree == None:
        return None
    
    if tree.right != None:
        return leftmost(tree.right)

    else:
        curr = tree
        parent = tree.parent
        while parent != None and curr != parent.right:
            curr = parent
            parent = parent.parent

    # Return the parent where this is a left subtree or None if there is
    # no right subtree and no parent that meets the criteria.
    return parent

    
# O(height) time | O(height) space
def leftmost(tree):
    if tree.right == None:
        return None

    curr = tree.right
    while curr.left.left != None:
        curr = curr.left

    return curr