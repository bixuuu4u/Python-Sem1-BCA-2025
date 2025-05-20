class A:
    def add(self,a,b,c=0):
        return a+b+c
    
obj =A()
print(obj.add(10,20))
print(obj.add(10,20,30))