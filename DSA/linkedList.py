class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
# A linked list class with a single head node
class linkedList:
    def __init__ (self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        # temperoray variable to iterate the elements in the linked list one by one
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)