class college:
    def __init__(self,name,branch,roll):
        self.name=name
        self.branch=branch
        self.roll=roll
    def display(self):
        print(f"Name-{self.name}\nBranch-{self.branch}\nBI-{self.roll}")


student1=college("Bisu","bCA","BI240434")

student1.display()

def input_students():
    students=[]
    counter=1
    while True:
        print("Enter Details")
        name=input(f"SN{counter} Enter Student Name")
        branch=input("Enter branch")
        roll=input("Enter BI number")

        student= college(name,branch,roll)

        students.append(student)

        choice=input("Press enter to enter more data or type No")
        if choice == 'No' or choice =='no':
            break
        counter +=1
    return students
    
main_list= input_students()

for student in main_list:
    student.display()
