import hash

# Example usage:
M = 10  # Size of the hash table
H = [None] * M  # Initialize an empty hash table

# Inserting elements into the hash table
hash.insert(5, H, M)
hash.insert(15, H, M)
hash.insert(25, H, M)

result = hash.search(15, H, M)
print(result)

print(H)

