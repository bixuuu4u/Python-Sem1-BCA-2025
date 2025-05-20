# Wap TO demonstrate both static and dynamic polymorphism in python

class A:
    def add(self,a,b):
        print("A")
        return a+b
class B:
    def add(self,a,b):
        print("B")
        return a+b
class C(A,B):
    def add(self,a,b):
        # super().add(a,b)
        print("C")
        return a+b
    
obj=C()

print(obj.add(3,4))