class A:
    # in this function we dont want to pass any arguments so we use staticmethod
    @staticmethod
    def greet1():
        print("Good morning")

a1=A()

a1.greet1()