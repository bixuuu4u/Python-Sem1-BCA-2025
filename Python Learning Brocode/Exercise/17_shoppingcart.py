#Shoppingg Cart Problem

foods=[]
prices=[]

total=0

while True:
    food = input("Enter a food to buy ![q to checkout]:\n")
    if (food =="q" or food=="Q"):
        # print("Hi")
        break
    else:
        # print("Hi")
        price= float(input(f"Enter price of a {food} $"))
        foods.append(food)
        prices.append(price)
print("------YOUR CART------")
# print(foods)

for counter in range(len(foods)):  
    
    print(f"{counter+1}:{foods[counter]}--{prices[counter]:.2f}")
    total=total+prices[counter]
print(f"Total is ${total}")