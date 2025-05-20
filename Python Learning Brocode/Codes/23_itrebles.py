#Itrebles =An object that can return its elements one at a time, aalowing it to be itreted over in a loop
#LIST
numbers=[1,2,3,4,5]

for number in numbers:  #descriptive name
    print(number,end=" ")
for number in reversed(numbers):  
    print(number,end=" ")
#TUPLE
tuple=(1,2,3,4,5)
for number in (tuple):  
    print(number,end="-")
#SETS
fruits={"Apple","Banana","Kela","Orange"}

for fruit in fruits:
    print(fruit)
#STRINGS
name ="Bisuu"

for char in name:
    print(char,end="  ")

print()
#DICTIONARY
my_dict={"A":1,"B":2}

for key in my_dict:
    print(key)


for value in my_dict.values():
    print(value)

for key,values in my_dict.items():
    print(key,values)