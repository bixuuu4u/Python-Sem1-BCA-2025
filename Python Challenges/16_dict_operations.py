# Program to Demonstrate Basic Operations on a Dictionary

# Creating a dictionary
student = {"name": "Alice", "age": 20, "course": "Computer Science"}

# Accessing elements
print("Name:", student["name"])

# Modifying values
student["age"] = 21
print("Updated age:", student["age"])

# Adding new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Deleting a key-value pair
del student["course"]
print("After deleting 'course':", student)

# Iterating over dictionary
for key, value in student.items():
    print(f"{key}: {value}")

