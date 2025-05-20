class student:
    def __init__(self,name,roll,course=[]):
        self.name=name
        self.roll=roll
        self.course=list(course)
    def display(self):
        print(f"Student Name-{self.name}")
        print(f"Roll-{self.roll}")        
        print(f"Course-{self.course}")
    def add_course(self):
        userinput=input("Enter Course To add:")
        self.course.append(userinput)
        print(f"Added Sussesfully:{userinput}")
    def remove_course(self):
        userinput=input("Enter Course to remove:")
        if userinput in self.course:
            self.course.remove(userinput)
            print(f"Removed successfully:{userinput}")
        else:
            print("Course not found")

s=student("Bisu",434,["bCa"])

s.display()
s.add_course()
s.remove_course()
s.display()