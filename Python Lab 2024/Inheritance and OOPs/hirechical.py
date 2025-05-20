# Hirechical Inheritance
class A:
    def __init__(self):
        pass
    def show(self):
        print("I am A")

class B(A):
    def __init__(self):
        pass
    def show(self):
        # super().show()

        print("I am B")

class C(A):
    def __init__(self):
        pass
    def show(self):
        # super().show()

        print("I am C")

class D(A):
    def __init__(self):
        pass
    def show(self):
        super().show()
        print("I am D")


obj=D()
B.show(obj)
C.show(obj)
obj.show()

