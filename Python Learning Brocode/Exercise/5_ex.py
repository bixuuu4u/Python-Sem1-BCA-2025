#Find Hypotenous of right angled tringle
# c= squrt(a^2 + b^2)
import math
a=float(input("Enter side a :"))
b=float(input("Enter side b :"))

c= math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenous is {round(c,2)}")