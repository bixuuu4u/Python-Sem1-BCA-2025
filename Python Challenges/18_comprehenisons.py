# Program to Demonstrate List, Set, and Dictionary Comprehensions

# List Comprehension: Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("List of squares:", squares)

# Set Comprehension: Extract unique vowels from a string
vowels = {char for char in "hello world" if char in "aeiou"}
print("Unique vowels:", vowels)

# Dictionary Comprehension: Create a dictionary with numbers and their squares
square_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of squares:", square_dict)
