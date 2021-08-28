from LinkedList import LinkedList
from Node import Node

# This time the lists are in the opposite order.
def sum_linked_list(l1, l2):
    equalize_list_lengths(l1, l2)
    dummy_head = Node(-1)
    carry = sum_recursive(l1.head, l2.head, dummy_head)
    if carry > 0:
        dummy_head.value = carry
        return LinkedList(dummy_head)
    ans = LinkedList(dummy_head.next)
    dummy_head.next = None
    return ans


def sum_recursive(node1, node2, prev):
    if node1 == None:
        return 0
    new_node = Node(0)
    total = node1.value if node1.value < 10 else 0
    total += node2.value if node2.value < 10 else 0
    total += sum_recursive(node1.next, node2.next, new_node)
    new_node.value = total % 10
    prev.next = new_node
    return total // 10

def equalize_list_lengths(l1, l2):
    add_to_l1 = 0
    add_to_l2 = 0
    l1_head = l1.head
    l2_head = l2.head
    curr1 = l1.head
    curr2 = l2.head
    while curr1 != None and curr2 != None:
        curr1 = curr1.next
        curr2 = curr2.next

    while curr1 != None:
        curr1 = curr1.next
        add_to_l2 += 1

    while curr2 != None:
        curr2 = curr2.next
        add_to_l1 += 1

    if add_to_l1 > 0:
        l1_head = Node(-1)
        curr = l1_head
        while add_to_l1 > 0:
            curr.next = Node(10)
            curr = curr.next
            add_to_l1 -= 1
        curr.next = l1.head
        l1_head = l1_head.next

    if add_to_l2 > 0:
        l2_head = Node(-1)
        curr = l2_head
        while add_to_l2 > 0:
            curr.next = Node(10)
            curr = curr.next
            add_to_l2 -= 1
        curr.next = l2.head
        l2_head = l2_head.next

    l1.head = l1_head
    l2.head = l2_head

test1 =  LinkedList(Node(1))
test1.add_node(Node(2))

test2 = LinkedList(Node(1))
test2.add_node(Node(2))
test2.add_node(Node(3))

print(test1)
print(test2)

print(sum_linked_list(test1, test2))

    
    