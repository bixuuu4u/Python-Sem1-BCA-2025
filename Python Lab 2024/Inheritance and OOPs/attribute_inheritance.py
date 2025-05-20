#2 Methods
class A:
    def __init__(self):
        self.name="Bisu"
class B:
    def __init__(self):
        self.roll="434"
class C(A,B):

    def display(self):
        
        print(f"Name-{self.name}")
        print(f"Roll-{self.roll}")
'''     def __init__(self):
        A.__init__(self)
        B.__init__(self)   '''


obj=C()

B.__init__(obj)
obj.display()
# print(obj.name)

# print(obj.roll)