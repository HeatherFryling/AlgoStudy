from LinkedList import LinkedList
from Node import Node

# O(n) time where n is the num items in the longer list.
# O(n) space for the list that gets returned.
def sum_linked_list(l1, l2):
    curr1 = l1.head
    curr2 = l2.head
    carry = 0
    dummy_head = Node(-1)
    curr_new = dummy_head

    while (curr1 != None and curr2 != None):
        total = curr1.value + curr2.value + carry
        carry = total // 10
        value = total % 10
        new_node = Node(value)
        curr_new.next = new_node
        curr_new = curr_new.next
        curr1 = curr1.next
        curr2 = curr2.next

    while (curr1 != None):
        total = curr1.value + carry
        carry = carry // 10
        value = total % 10
        new_node = Node(value)
        curr_new.next = new_node
        curr_new = curr_new.next
        curr1 = curr1.next

    while (curr2 != None):
        total = curr2.value + carry
        carry = carry // 10
        value = total % 10
        new_node = Node(value)
        curr_new.next = new_node
        curr_new = curr_new.next
        curr2 = curr2.next

    if carry > 0:
        new_node = Node(carry)
        curr_new.next = new_node
    
    return LinkedList(dummy_head.next)

test1_1 = LinkedList(Node(3))
test1_2 = LinkedList(Node(9))

print(sum_linked_list(test1_1, test1_2))

test2_1 = LinkedList(Node(7))
test2_1.add_node(Node(1))
test2_1.add_node(Node(6))

test2_2 = LinkedList(Node(5))
test2_2.add_node(Node(9))
test2_2.add_node(Node(2))

print(sum_linked_list(test2_1, test2_2))

test3_1 = LinkedList(Node(7))
test3_1.add_node(Node(1))

test3_2 = LinkedList(Node(5))
test3_2.add_node(Node(9))
test3_2.add_node(Node(2))

print(sum_linked_list(test3_1, test3_2))

test4_1 = LinkedList(Node(7))
test4_1.add_node(Node(1))
test4_1.add_node(Node(6))

test4_2 = LinkedList(Node(5))
test4_2.add_node(Node(9))

print(sum_linked_list(test4_1, test4_2))

test5_1 = LinkedList(Node(9))
test5_1.add_node(Node(7))
test5_1.add_node(Node(8))

test5_2 = LinkedList(Node(6))
test5_2.add_node(Node(8))
test5_2.add_node(Node(5))

print(sum_linked_list(test5_1, test5_2))
