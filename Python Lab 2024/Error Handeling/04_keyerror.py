dict={"1":"Py","2":"java"}
try:
    print(dict)
    key=input("Enter key :")
    print(dict[key])
except:
    print("Key not found in dictionatry")
else:
    print("Key Found")
finally:
    print("Thank You!")
