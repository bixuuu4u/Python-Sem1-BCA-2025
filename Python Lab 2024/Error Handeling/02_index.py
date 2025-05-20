list=[1,2,3]
try:
    a=list[8]   
except :
    print("Index Error")
else:
    print("Result=",a)
finally:
    print("Thank You!")