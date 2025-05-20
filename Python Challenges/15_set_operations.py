#  Program to Demonstrate Basic Operations on a Set

# Creating sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Basic set operations
print("Union:", A | B)  # or A.union(B)
print("Intersection:", A & B)  # or A.intersection(B)
print("Difference (A - B):", A - B)  # or A.difference(B)
print("Symmetric Difference:", A ^ B)  # or A.symmetric_difference(B)

# Adding and removing elements
A.add(10)
print("After adding 10:", A)
A.remove(2)
print("After removing 2:", A)

# Checking membership
print("Is 3 in set A?", 3 in A)
