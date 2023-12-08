import hash

table = hash.HashTable(10)

# Inserting elements into the hash table
table.insertV2(3)
table.insertV2(5)
table.insertV2(49)
table.insertV2(15)
table.insertV2(25)

table.display_table()

result = table.searchV2(15)


table.eagerDelete(25)

result = table.searchV2(25)

table.display_table()

if result is not None:
    print(f"Value {result} found in the hash table. Result: {result}")
else:
    print("Value not found in the hash table.")



