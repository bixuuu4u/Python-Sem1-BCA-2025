class Calc:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"Square is {self.n**2}")
    def cube(self):
        print(f"Cube is {self.n**3}")
        
    def sqrt(self):
        print(f"SquareRoot is {self.n**1/2}")

c1=Calc(4)
c1.square()
c1.cube()
c1.sqrt()



