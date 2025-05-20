#2dlist = [list1,list2,list3]

fruits = ["Apple", "Banana", "Orange", "Grapes"]
vegetables = ["Carrot", "Broccoli", "Spinach", "Potato"]
meats = ["Chicken", "Beef", "Pork", "Fish"]


# print("Fruits:", fruits)
# print("Vegetables:", vegetables)
# print("Meats:", meats)

# groceries =[fruits,vegetables,meats]
groceries =[
    ["Apple", "Banana", "Orange", "Grapes"],
    ["Carrot", "Broccoli", "Spinach", "Potato"],
    ["Chicken", "Beef", "Pork", "Fish"]]
print(groceries,"\n")
print(groceries[0])
print(groceries[1])
print(groceries[2])
print()
print(groceries[1][0])

for i in range(len(groceries)):
    for j in range(len(groceries)):
        print(groceries[i][j],end =" ")
    print()