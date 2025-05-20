#Concession Stand
menu={ "Pizza":3.50,
      "Nachos":4.50,
      "Popcorn":6.00,
      "Fries":2.50,
      "Chips":1.00,
      "Soda":3.00,
      "Lemonde":4.69}
user_cart=[]

total=0

print("-------------MENU--------------")

for key ,value in menu.items():
    print(f"{key:7}: ${value:}")
print("-------------------------------")


while True:
    food =input("Select an item [q to quit]").capitalize()
    if food=="q" or food=="Q":
        break
    elif menu.get(food) is not None:
        user_cart.append(food)
    
# print(user_cart)

for food in user_cart:
    total  += menu.get(food)
    # print(food,end=" ")

print(f"Your total is {total}")