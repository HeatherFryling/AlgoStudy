from bst_node import BST_Node

# Given a sorted array, return a BST of minimal height.
# O (logn) time | O(n) space for the tree. O(logn) space on the call stack.
def minimal_tree(arr, start, stop):
    if stop < start:
        return None
    
    mid = start + (stop - start) // 2

    root = BST_Node(arr[mid])

    root.left = minimal_tree(arr, start, mid - 1)
    root.right = minimal_tree(arr, mid + 1, stop)
    return root


test1 = [1, 2, 3]
test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans1 = minimal_tree(test1, 0, len(test1) - 1)
ans1.print_bst()

ans2 = minimal_tree(test2, 0, len(test2) - 1)
ans2.print_bst()


