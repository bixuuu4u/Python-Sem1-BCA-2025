import math
class Calculator:


    def __init__(self,number):
        self.num= number

    def squre(self):
        return self.num**2
    def cube(self):
        return self.num**3
    def squreroot(self):
        return math.sqrt(self.num)
n=9
c=Calculator(n)

print(f"Squre of {n} is {c.squre()}")
print(f"Cube of {n} is {c.cube()}")
print(f"Squreroot of {n} is {c.squreroot()}")
print(f"")