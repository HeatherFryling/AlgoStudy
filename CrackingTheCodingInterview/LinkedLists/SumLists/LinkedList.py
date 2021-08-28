class LinkedList:
   
    def __init__(self, head):
        self.head = head

    def __str__(self):
        curr = self.head
        if curr == None:
            return 'None'
        str_lst = []
        while(curr != None):
            str_lst.append(str(curr.value))
            curr = curr.next
        return "LinkedList: " + str(str_lst)

    def add_node(self, node):
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        curr.next = node

