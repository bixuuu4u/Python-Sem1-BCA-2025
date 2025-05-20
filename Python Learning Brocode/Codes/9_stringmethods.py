

name =input("Enter your full name :")
#Length
name_lenght= len(name)
print(f"Lenght of your name is {name_lenght}")


#Find -1 if non found
space =name.find("b")
   #first occurance
print(space)
   #last occurance 
space =name.rfind("b")
print(space)



#Capitalize  first letter is capitialized
capitalize = name.capitalize()
print(capitalize)


#UPPER  upper case all 
up= name.upper()
print(up)


#Lower lower case all 
low= name.lower()
print(low)


#isdigit returns true or false  contains only number thn true
check = name.isdigit()
print(check)


#isalpha returns true or false  contains only char then true if space is in betn name then also false if number then also false  bisu123 is also false
check = name.isalpha()
print(check)


#count method counts for a string in a input
otp =input("Enter otp :")
result = otp.count("-")
print(result)

#replace replacese any string with another
name_2 = name.replace(" ","-")
print(name_2)



#for more information 
# print(help(str))