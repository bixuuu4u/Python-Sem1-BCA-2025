#if -- Do some code if some condition is true 
# Else do something else

age = int(input("Enter your age:: "))
if age>100:
    print("You are too old")
    
elif age<0:
    print("You havent been born yet")    
elif age>=18:
        
    print("You are 18 or 18+")    
else:
    print("You are 18-")    
user_name =input("Enter your name :: ")
if user_name=="":
    print("You didnt enter your name")
else:
    print(f"Hell-o  {user_name}")

user_response =input("Would you like to have some food ?:[Y/n]")
if user_response=="Y":
    print("Then have some ")
else:
    print("Your friend will pay have some food please")
