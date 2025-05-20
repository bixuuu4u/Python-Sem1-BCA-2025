#  Write a program to find out whether the integer entered by the user, through the
# keyboard, is even or odd number.

# Taking user input
num = int(input("Enter an integer: "))

# Method 1: Using Modulus Operator
if num % 2 == 0:
    print("Method 1: The number is Even")
else:
    print("Method 1: The number is Odd")

# Method 2: Using Bitwise AND Operator
if num & 1 == 0:
    print("Method 2: The number is Even")
else:
    print("Method 2: The number is Odd")

num = int(input("Enter a number: "))
if (num / 2) * 2 == num:
    print("Even using Division & Multiplication")
else:
    print("Odd using Division & Multiplication")

if (num // 2) * 2 == num:
    print("Even using Floor Division")
else:
    print("Odd using Floor Division")

if (num ^ 1) == num + 1:
    print("Even using XOR")
else:
    print("Odd using XOR")

if (num >> 1) << 1 == num:
    print("Even using Bitwise Shift")
else:
    print("Odd using Bitwise Shift")

