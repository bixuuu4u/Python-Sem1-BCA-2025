class A:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("A")
    
class B(A):
    def __init__(self,roll):
        self.roll=roll
    def show(self):
        print("B")
class C:
    def __init__(self,course):
        self.course=course
    def show(self):
        print("C")
class D(B,C):
    def __init__(self):
        pass
    def show(self):
        print("D")
A("Bisu")
obj =D()

obj.show()
print(D.mro())