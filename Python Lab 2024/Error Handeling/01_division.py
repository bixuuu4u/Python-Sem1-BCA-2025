a=int(input("Enter a number: "))
try:
    result = 5/a    
except :
    print("Division by zero not possible")
else:
    print("Result=",result)
finally:
    print("Thank You!")