class A:
    def add(self,*args):
        return sum(args)
obj=A()
print(obj.add(1))
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))
print(obj.add(1,2,3,4,5))    