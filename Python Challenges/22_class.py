# Python Class "Student" with Various Attributes and Methods

class Student:
    def __init__(self, name, roll_no, age, marks):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Age: {self.age}, Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40

# Creating a student object
student1 = Student("John", 101, 18, 85)

# Display student details
student1.display_info()

# Check if student passed
print("Passed" if student1.is_passed() else "Failed")
