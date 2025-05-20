#  Program to Sort List of Students Based on Roll Number
# Creating a list of students (each student is represented as [name, roll, age])
# Creating a list of students (each student is represented as [name, roll, age])
students = [
    ["Amit", 103, 20],
    ["Rohan", 101, 21],
    ["Neha", 105, 19],
    ["Sara", 102, 22],
    ["Vikram", 104, 20]
]

# Sorting based on Roll Number (index 1)
students.sort(key=lambda x: x[1])

# Displaying sorted students
print("Students sorted by Roll Number:")
for student in students:
    print(f"Name: {student[0]}, Roll No: {student[1]}, Age: {student[2]}")

