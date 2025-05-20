#Collection - Single 'variable' used to store multiple values
#   Set   = () Unordered and immutable,Add/Removw OK. Duplicates NO
#   Tuple = {} Ordered and unchangable.Duplicates OK
#   List  = [] Ordered and Changable. Duplicates OK


fruits=["Apple","Orange","banana","Kela","Amrut"]
# print(type(fruit))
print(len(fruits))

        #if out of index then Index Error
# print(dir(fruits))
# print(help(fruits))
# print(fruits[::-1])
for fruit in fruits:
    print(fruit)

check = "Apple" in fruits
print(check)
fruits[0]="Seb"


#Methods in a LIST

fruits.append("Kadali")

fruits.remove("Orange")

fruits.insert(0,"Angooor")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
print(fruits.count("Kela"))
print(fruits.index("Kela"))#error if no value
print(fruits)
