#Shopping cart Problem

item= input("What are you buying ?: ")

price= float(input("What is the price of the product?: "))

quantity = int(input("How many of them would you like to have?:"))


total = price * quantity
print(f"You have brought {quantity} x {item}")
print(f"Your total is {total}")
