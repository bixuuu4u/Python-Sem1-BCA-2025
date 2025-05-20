#return -Statement used to end a function
#          and sentd a result back to the caller

#add substract multiply divide
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
    

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

result=add(num1,num2)
print("Sum is ",result)
result=substract(num1,num2)
print("Substrection is ",result)
result=multiply(num1,num2)
print("Multiplication is ",result)
result=divide(num1,num2)
print("Division is ",result)