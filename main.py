import hash

table = hash.HashTable(10)

# Inserting elements into the hash table
table.insertV2(5)
table.insertV2(15)
table.insertV2(25)

table.display_table()

result = table.search(15)

if result is not None:
    print(f"Value {result} found in the hash table. Result: {result}")
else:
    print("Value not found in the hash table.")



