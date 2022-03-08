# hash function
# def get_hash(key):
#     h = 0
#     for char in key:
#         # ord gives the ASCII value
#         h += ord(char)
#         # assume size of the list is 100
#     return h % 100
# print(get_hash('march 28'))

class HashTable:
    # list comprehension offers a shorter syntax
    # newlist = [expression for item in iterable if condition == True]
    def __init__(self):
        self.max = 100
        self.arr =[None for i in range(self.max)]
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    # implement function to add and get an item from the hash table
    # key value pair
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]






