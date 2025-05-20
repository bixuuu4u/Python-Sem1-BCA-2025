# User enters numbers and operator to perform calculation

num1=float(input("Enter 1st number :"))
num2=float(input("Enter 2nd number :"))
operator=input("Enter an operator [+ | - | * | / | %] :")


if operator == "+":
    result = num1+ num2
    print(f"{num1} + {num2}={num1 +num2}")
elif operator == "-":
    result = num1- num2
    print(f"{num1} - {num2}={num1- num2}")

elif operator == "*":
    result = num1* num2
    print(f"{num1} * {num2}={num1* num2}")


elif operator == "/":
    result = num1 /num2
    print(f"{num1} / {num2}={num1/ num2}")


elif operator == "%":
    result = num1 %num2
    print(f"{num1} % {num2}={num1 %num2}")


else:
    print(f"Error!! {operator} is not a valid operator")
    print("Rerun the code and enter from the options")

