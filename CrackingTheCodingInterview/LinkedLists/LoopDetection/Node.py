class Node:

    def __init__(self, val = None):
        self.value = val
        self.next = None

    def __str__(self):
        return "Node: " + str(self.value)
    
    def __repr__(self):
        return "Node: " + str(self.value)