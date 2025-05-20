#Calculate area of the Circle
# A= piR^2
import math

radius = float(input("Enter radius of the circle : "))
area= math.pi * pow(radius,2)
print(f"The area of the cirle is {round(area,2)}")