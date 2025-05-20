#Validate user input exercise
#1. usernameis no more than 12 character
#2. username must not contain spaces
#3. user name must not contain digits



username= input("Enter your name :: ")




if len(username) >12:
    print("Accessed Deined")
    print(f"{username} Contains more than 12 charcater")
elif not username.find(" ") ==-1:
    print("Accessed Denied")
    print(f"{username} must not contain any spaces")

elif username.isdigit():
    print("Accessed Deined")
    print(f"{username}  digits  is not accepted")
    
elif not(username.isalpha()):
    print("Accessed Deined")
    print(f"{username} Contains numbers")

else:
    print("Acces Granted")
    print(f"{username} Welcome !!")





