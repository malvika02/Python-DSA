class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# A linked list class with a single head node
class linkedList:
    def __init__ (self):
        self.head = None
# creating a single node 
first = node(3)
print(first.data)