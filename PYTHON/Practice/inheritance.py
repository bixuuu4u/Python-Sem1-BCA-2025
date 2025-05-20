class A:
    def __init__(self):
        self.name="Bisu"
    def showa(self):
        print("I am in A")

class B(A):
    def __init__(self):
        super().__init__()
        self.name="Bimbim bum bam"
    def showb(self):
        print("I am in B")

obj = B()

obj.showa()
obj.showb()
print(obj.name)