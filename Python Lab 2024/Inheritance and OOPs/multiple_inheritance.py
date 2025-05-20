class A:
    def show(self):
        print("I am A")
class B:
    def show(self):
        #super().show()
        print("I am B")
class C(A,B):
    def  show(self):
        super().show()
        print("I am C")

obj=C()
obj.show()
B.show(obj)