# Program to Demonstrate Basic Operations on a Tuple

# Creating a tuple
numbers = (10, 20, 30, 40, 50)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Tuple slicing
subset = numbers[1:4]  # Extracts elements from index 1 to 3

# Count and index methods
print("Count of 20:", numbers.count(20))
print("Index of 40:", numbers.index(40))

# Tuple concatenation
new_tuple = numbers + (60, 70)
print("Concatenated tuple:", new_tuple)

# Tuple unpacking
a, b, c, d, e = numbers
print("Unpacked values:", a, b, c, d, e)
