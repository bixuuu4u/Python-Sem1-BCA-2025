a=input("Enter a number:")

try:
    b= a+2
except:
    print("Type of a is string must be integer")
else:
    print(b)
finally:
    print("Thank You")
