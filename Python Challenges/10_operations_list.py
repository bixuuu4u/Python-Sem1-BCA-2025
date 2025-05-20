# Write a program to demonstrate basic operations on the list.

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding elements
numbers.append(60)
numbers.insert(2, 25)  # Insert 25 at index 2

# Removing elements
numbers.remove(30)  # Removes first occurrence of 30
deleted = numbers.pop()  # Removes and returns the last element

# Slicing
subset = numbers[1:4]  # Extracts elements from index 1 to 3

# List Operations
print("Modified list:", numbers)
print("Deleted element:", deleted)
print("Sliced part:", subset)
print("Reversed list:", numbers[::-1])
print("Sum of list:", sum(numbers))
