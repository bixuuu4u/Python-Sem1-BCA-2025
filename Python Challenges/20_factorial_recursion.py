# Program to Find Factorial Using Recursion

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Input from user
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial_recursive(num)}")
