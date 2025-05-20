#  Write a program that will find the roots of a quadratic equation: ax² + bx + c = 0

import math

# Input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Check the nature of the roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots are real and different: {root1:.2f}, {root2:.2f}")

elif discriminant == 0:
    # One real root (both roots are same)
    root = -b / (2 * a)
    print(f"Roots are real and same: {root:.2f}")

else:
    # Complex roots
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"Roots are complex: {real_part:.2f} ± {imag_part:.2f}i")

