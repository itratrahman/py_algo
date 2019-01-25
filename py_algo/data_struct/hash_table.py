
class HashTable(object):
    """
    Class module of Hash Table
    """
    def __init__(self):
        """
        Class constructor which initialize size
        and the lists to store the keys and values
        of the HashTable
        """
        # size of the HashTable
        self.size = 11
        # list to store the keys
        self.slots = [None]*self.size
        # list to store the values
        self.data = [None]*self.size

    def hashfunction(self, key, size):
        """
        Method to compute hash function
        """
        return key%size

    def rehash(self, oldhash, size):
        """
        Method to compute rehash on the event of a collision
        """
        return (oldhash+1)%size

    def put(self, key, data):
        """
        Method to put i.e. insert key value pair into Hash Table
        """
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data

    def get(self,key):
        """
        Method to get value of the key from the HashTable if the key is present
        """
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        """
        Get method
        """
        return self.get(key)

    def __setitem__(self,key,data):
        """
        Set method
        """
        self.put(key,data)

if __name__ == "__main__":
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H[20])
    print(H[17])
    H[20]='duck'
    print(H[20])
    print(H.data)
    print(H[99])
