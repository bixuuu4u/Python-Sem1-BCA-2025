fruits={"Apple","Orange","Orange","Orange","Orange""banana","Kela","Amrut"}
# print(type(fruits))
# print(dir(fruits))
# print(help(fruits))
print(fruits)
print(len(fruits))

check = "Apple" in fruits
print(check)

#print(fruits[1]) #TypeError: 'set' object is not subscriptable
fruits.add("Idli")
fruits.remove("Kela")

fruits.pop()
# fruits.clear()

print(fruits)
