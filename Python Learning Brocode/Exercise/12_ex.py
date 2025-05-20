#Temp Convertor

temp = float(input("Enter temperature :"))
unit = input("Enter unit [C/F] : ").upper()

if unit=="C":
    f=((9*temp) /5) +32
    new_unit="F"
    print(f"{temp} {unit} is {round(f,3)} {new_unit}")
elif unit=="F":
    c=(temp-32)* 5/9
    new_unit="C"
    print(f"{temp} {unit} is {round(c,3)} {new_unit}")

else:
    print(f"{unit} is not valid !!")