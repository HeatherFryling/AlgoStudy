class BST_Node_Parent_Included:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    def print_bst(self):
        output = []
        self.dfs_print_helper(output, self)
        print('BST:', output)



    def dfs_print_helper(self, lst, node):
        if node == None:
            return
        self.dfs_print_helper(lst, node.left)
        lst.append(node.value)
        self.dfs_print_helper(lst, node.right)
