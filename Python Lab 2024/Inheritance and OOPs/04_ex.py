class Student:
    def __init__(self,name,roll,course):
        self.name=name
        self.roll=roll
        self.course=course
    def display(self):
        print(f"Name-{self.name}")
        print(f"Roll-{self.roll}")
        print(f"Course-{self.course}")
    def change_course(self,new_course):
        self.course=new_course

s1=Student("Bisu",42434,"Bca")
s1.display()
s1.change_course("mca")
s1.display()