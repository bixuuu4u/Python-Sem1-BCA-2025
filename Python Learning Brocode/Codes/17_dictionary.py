#Dixctionary -- A collection of {key:value} pairs 
#        Ordered and changable  :No duplicates


capitals={"USA":"Washington D.C",
          "India":"New Delhi",
          "Russia":"Moscow",
          }
# print(dir(capitals))
# print(help(capitals))
print(capitals)

print(capitals.get("USA"))
print(capitals.get("Japan")) #None

# if capitals.get("India"):
#     print("That cacpital exists")
# else:
#     print("That cacpital doesnt exists")


capitals.update({"Germany":"Berlin"}) #add or modify using update
capitals.update({"USA":"BC"})
capitals.pop("Russia")
# capitals.clear()


keys=capitals.keys()

# for key in capitals.keys():
#     print(key)
# print(keys)
# print(capitals)

values = capitals.values()
for valeu in values:
    print(valeu)
print(values)


items = capitals.items()
print(items)   #@d list of tupels

for key,value in capitals.items():
    print(f"{key}:{value}")