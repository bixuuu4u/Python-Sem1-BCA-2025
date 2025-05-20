# Given three points (x1, y1), (x2, y2), (x3, y3), write a program to check all the three
# points fall on one straight line.

# Taking input from the user
x1, y1 = map(int, input("Enter x1, y1: ").split())
x2, y2 = map(int, input("Enter x2, y2: ").split())
x3, y3 = map(int, input("Enter x3, y3: ").split())

# Using the collinearity condition (Area of triangle method)
area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

# Checking if the area is zero
if area == 0:
    print("The three points lie on a straight line.")
else:
    print("The three points do not lie on a straight line.")
