class A:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return A(self.value + other.value) 
obj=A(10)
obj1=A(20)
result=obj1+obj

print("Result=",result)
print("Result=",result.value)
