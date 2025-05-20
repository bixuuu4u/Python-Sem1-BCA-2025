# Demonstration of Static and Dynamic Polymorphism in Python

# Static Polymorphism (Method Overloading - Achieved Using Default Arguments)

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c  # If c is not passed, it defaults to 0

math_op = MathOperations()
print("Sum of 2 numbers:", math_op.add(5, 10))
print("Sum of 3 numbers:", math_op.add(5, 10, 15))
