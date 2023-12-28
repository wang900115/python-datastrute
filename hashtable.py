class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = [None]*self.size

    def _hash(self,key):
        return hash(key) % self.size

    def print_table(self):
        for index ,slot in enumerate(self.hash_table):
            print(f'Index{index}:{slot}')

    def insert(self,key,value):
        index = self._hash(key)
        if self.hash_table[index]  is None:
            self.hash_table[index] = [(key,value)]
        else:
            for i,pair in enumerate(self.hash_table[index]):
                if pair[0] == key:
                    self.hash_table[index][i] = (key,value)
                    return
            self.hash_table[index].append((key,value))
    def search(self,key):
        index = self._hash(key)
        if self.hash_table[index] is not None:
            for pair in self.hash_table[index]:
                if pair[0]==key:
                    return pair[1]
        return None

    def delete(self,key):
        index = self._hash(key)
        if self.hash_table[index] is not None:
            for i,pair in enumerate(self.hash_table[index]):
                if pair[0]==key:
                    del self.hash_table[index][i]
                    return
        return None


hash_table = HashTable(10)
hash_table.insert('a',5)
hash_table.insert('b',6)
hash_table.insert('c',7)
hash_table.insert('d',7)
hash_table.insert('e',5)
hash_table.insert('f',6)
hash_table.insert('z',7)
hash_table.insert('a',7)


hash_table.print_table()



