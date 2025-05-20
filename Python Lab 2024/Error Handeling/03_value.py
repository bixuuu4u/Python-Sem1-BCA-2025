list=[1,2,3]
try:
    print(list)
    num= int(input("Enter a number to remove from list: ")) 
    list.remove(num)  
except:
    print("Value error number not found in list")
else:
    print("Number removed ",num)
    print(list)
finally:
    print("Thank You!")
