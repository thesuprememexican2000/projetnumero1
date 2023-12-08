
DELETED = "DELETED"


class HashTable():

    def __init__(self, table_size):
        self.__table_size = table_size
        self.__hash_table = [None] * table_size  # implementation d'un tableau en python

    def hash(self, key: int):
        hashcode = key % self.__table_size
        return hashcode

    def insert(self, x):
        i = self.hash(x)

        if self.__hash_table[i] is None:
            self.__hash_table[i] = x
        else:
            while self.__hash_table[i] is not None:
                i = (i + 1) % self.__table_size
                self.__hash_table[i] = x

    def search(self, x):
        i = self.hash(x)
        while self.__hash_table[i] is not None:
            if self.__hash_table[i] == x:
                return self.__hash_table[i]  # Return the value if found
            i = (i + 1) % self.__table_size
        return None  # Return None if the element is not found

    def eagerDelete(self, x):
        i = self.hash(x)
        while self.__hash_table[i] is not None:
            if self.__hash_table[i] == x:
                # Perform eager deletion
                self.__hash_table[i] = None
                shift_position = i
                next_position = (i + 1) % self.__table_size

                while self.__hash_table[next_position] is not None:
                    if self.hash(self.__hash_table[next_position]) <= i:
                        self.__hash_table[shift_position] = self.__hash_table[next_position]
                        shift_position = next_position
                    next_position = (next_position + 1) % self.__table_size

                self.__hash_table[shift_position] = None
                return

            i = (i + 1) % self.__table_size

    def lazyDelete(self, x):
        i = self.hash(x)
        while self.__hash_table[i] is not None:
            if self.__hash_table[i] == x:
                self.__hash_table[i] = DELETED
                return
            i = (i + 1) % self.__table_size

    def insertV2(self, x):
        i = self.hash(x)
        if self.__hash_table[i] is None or self.__hash_table[i] == DELETED:
            self.__hash_table[i] = x
        else:
            while self.__hash_table[i] is not None and self.__hash_table[i] != DELETED:
                i = (i + 1) % self.__table_size
                print(i)
                self.__hash_table[i] = x

    def searchV2(self, x):
        i = self.hash(x)
        while self.__hash_table[i] is not None:
            if self.__hash_table[i] == x:
                return self.__hash_table[i]
            i = (i + 1) % self.__table_size
        return None

    def display_table(self):
        print("Hash Table:")
        for i, entry in enumerate(self.__hash_table):
            print(f"Index {i}: {entry}")


