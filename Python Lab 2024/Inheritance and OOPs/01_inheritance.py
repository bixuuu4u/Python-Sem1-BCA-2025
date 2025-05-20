# Inheritance is a feature in OOP where a child class (subclass)
# inherits properties and methods from a parent class (superclass).
#  It promotes code reusability and hierarchical relationships between classes.


# Single inheritance
class A:
    def __init__(self):
        pass
    def show_a(self):
        print("I am A")
class B(A):
    def __init__(self):
        pass
    def show_b(self):
        print("I am B")

obj=B()
obj.show_a()
obj.show_b()

    