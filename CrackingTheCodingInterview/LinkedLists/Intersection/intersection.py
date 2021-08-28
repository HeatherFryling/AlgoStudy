from LinkedList import LinkedList
from Node import Node

# O(n + m) time | O(1) space
def list_intersection(lst1, lst2):
    if lst1.head == lst2.head:
        return lst1.head
    tail1, length1 = get_tail_and_length(lst1)
    tail2, length2 = get_tail_and_length(lst2)

    if tail1 != tail2:
        return None
    
    diff = abs(length1 - length2)

    pos1 = lst1.head
    pos2 = lst2.head

    if length1 > length2:
        pos1 = advance_by_k(pos1, diff)
    else:
        pos2 = advance_by_k(pos2, diff)

    while (pos1 != pos2):
        pos1 = pos1.next
        pos2 = pos2.next

    return pos1

def advance_by_k(node, k):
    curr = node
    while (k > 0):
        k -= 1
        curr = curr.next
    return curr

def get_tail_and_length(lst):
    if lst.head == None:
        return 0
    curr = lst.head
    length = 1
    while(curr.next != None):
        length += 1
        curr = curr.next
    return curr, length

test1 = LinkedList(Node(1))
test1.add_node(Node(2))
test1.add_node(Node(3))

test2 = LinkedList(Node(1))
test2.add_node(Node(2))
test2.add_node(Node(3))

print(list_intersection(test1, test2))

short = LinkedList(Node(1))

long = LinkedList(Node(15))
long.add_node(Node(2))
long.add_node(Node(3))
long.add_node(Node(4))
long.add_node(short.head)

print(list_intersection(short, long))
print(list_intersection(long, short))

short.add_node(Node(3))

print(list_intersection(short, long))
print(list_intersection(long, short))

short.add_node(Node(3))
short.add_node(Node(3))
short.add_node(Node(3))
short.add_node(Node(3))

print(list_intersection(short, long))
print(list_intersection(long, short))
