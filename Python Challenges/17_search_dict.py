# Program to Search for a Student in a Dictionary


# Creating dictionary with roll number as key and student details as value
students = {
    101: ["Alice", "CS"],
    102: ["Bob", "IT"],
    103: ["Charlie", "ECE"]
}

# Input from user
search_name = input("Enter the name of the student to search: ")

# Searching for the student
found = False
for roll, details in students.items():
    if details[0] == search_name:
        print(f"Student found: Roll No: {roll}, Name: {details[0]}, Course: {details[1]}")
        found = True
        break

if not found:
    print("Student not found!")
