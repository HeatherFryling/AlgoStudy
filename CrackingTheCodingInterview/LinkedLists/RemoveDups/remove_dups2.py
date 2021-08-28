from LinkedList import LinkedList
from Node import Node

# O(n^2) time | O(1) space
def remove_dups2(lst):
    slow = lst.head
    count = 0
    while slow != None:
        fast = slow.next
        fast_prev = slow
        while fast != None:
            if fast.value == slow.value:
                count += 1
                remove_node(fast_prev, fast, lst)
            else:
                fast_prev = fast
            fast = fast.next
        slow = slow.next

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

remove_dups2(test1)
print(test1)

# Test a dup at the end.
test2 = LinkedList(Node(1))
test2.add_node(Node(2))
test2.add_node(Node(3))
test2.add_node(Node(4))
test2.add_node(Node(2))
print(test2)

remove_dups2(test2)
print(test2)

# Test all dups.
test3 = LinkedList(Node(1))
test3.add_node(Node(1))
test3.add_node(Node(1))
test3.add_node(Node(1))
test3.add_node(Node(1))

print(test3)

remove_dups2(test3)
print(test3)
