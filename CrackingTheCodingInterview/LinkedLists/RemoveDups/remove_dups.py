from LinkedList import LinkedList
from Node import Node

# O(n) time | O(n) space
def remove_dups(lst):
    seen = set({})
    prev = None
    curr = lst.head
    while curr != None:
        if curr.value not in seen:
            seen.add(curr.value)
            prev = curr
        else:
            remove_node(prev, curr, lst)
        curr = curr.next

def remove_node(prev, node, lst):
    if prev == None:
        lst.head = lst.head.next
        return
    prev.next = node.next

# Test a dup in the middle.
test1 = LinkedList(Node(1))
test1.add_node(Node(2))
test1.add_node(Node(3))
test1.add_node(Node(2))
test1.add_node(Node(4))
print(test1)

remove_dups(test1)
print(test1)

# Test a dup at the end.
test2 = LinkedList(Node(1))
test2.add_node(Node(2))
test2.add_node(Node(3))
test2.add_node(Node(4))
test2.add_node(Node(2))
print(test2)

remove_dups(test2)
print(test2)

# Test all dups.
test3 = LinkedList(Node(1))
test3.add_node(Node(1))
test3.add_node(Node(1))
test3.add_node(Node(1))
test3.add_node(Node(1))

print(test3)

remove_dups(test3)
print(test3)
