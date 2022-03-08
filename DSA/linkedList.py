from logging import raiseExceptions


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
        # temporary variable to iterate the elements in the linked list one by one
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + ' ---> '
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        # when there is no elements present in the list
        if self.head is None:
            self.head = Node(data, None)
            return
        # when there are elements present in list
        # temporary variable to iterate into the list and get to the last element
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    # input values it will create a new list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            # pointing to the next element
            self.head = self.head.next
            return
        # In linked list we have to maintain the count manually
        count = 0
        itr = self.head
        while itr:
            # we stop at the previous element
            if count == index-1:
                # previous element next link is pointing to this particular index that i am trying to remove
                # once the element is removed it will point to the next element next
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    # insert values at a particular index
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = linkedList()
    ll.insert_at_beginning(32)
    ll.insert_at_beginning(222)
    ll.insert_at_end(2445)
    ll.insert_at_end(3)
    ll.insert_at_end(["India", "America", "Australia", "Canada", "UAE"])
    ll.remove(2)
    ll.remove(12)
    # insert at a particular index(index, "value")
    ll.insert_at(0, "[Hello, everyone]")
    ll.print()
    print("length", ll.get_length())

