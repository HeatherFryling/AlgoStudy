from LinkedList import LinkedList
from Node import Node

def partition(ls, value):
    lesser_head = Node(-1)
    greater_head = Node(-1)

    curr_lesser = lesser_head
    curr_greater = greater_head

    curr = ls.head
    while(curr != None):
        next_to_check = curr.next
        if curr.value < value:
            curr_lesser.next = curr
            curr_lesser = curr_lesser.next
            curr_lesser.next = None
        if curr.value >= value:
            curr_greater.next = curr
            curr_greater = curr_greater.next
            curr_greater.next = None
        curr = next_to_check
    curr_lesser.next = greater_head.next
    greater_head.next = None
    ls.head = lesser_head.next

test1 = LinkedList(Node(5))
test1.add_node(Node(4))
test1.add_node(Node(3))
test1.add_node(Node(2))
test1.add_node(Node(1))
print(test1)

partition(test1, 3)
print(test1)

test2 = LinkedList(Node(3))
test2.add_node(Node(4))
test2.add_node(Node(1))
test2.add_node(Node(5))
test2.add_node(Node(2))
print(test2)

partition(test2, 3)
print(test2)

test3 = LinkedList(Node(5))
test3.add_node(Node(4))
test3.add_node(Node(3))
test3.add_node(Node(2))
test3.add_node(Node(1))
print(test3)

partition(test3, 5)
print(test3)