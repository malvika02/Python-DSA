class HashTable:
    # list comprehension offers a shorter syntax
    # newlist = [expression for item in iterable if condition == True]
    def __init__(self):
        self.max = 100
        self.arr =[[] for i in range(self.max)]
        # print(self.arr)
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    #  add function to add an item to the hash table
    #  key value pair
    def add(self, key, val):
        # index value 
        h = self.get_hash(key)
        value = [key, value]

        if 
        
    
    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]






