# Logical operators --- Evaluate multiple conditions
#                  or -- at least one conditions must be ture
#                  and  --- Both conditions must be true
#                  not --- inverts the conditions not True , not False
bool1 =True
bool2= False

print("Truth table of OR operator ")
print(f"{bool2} {bool2} {bool2 or bool2}")
print(f"{bool2} {bool1} {bool2 or bool1}")
print(f"{bool1} {bool2} {bool1 or bool2}")
print(f"{bool1} {bool1} {bool1 or bool1}")
print("*************************************")
print("Truth table of AND operator ")
print(f"{bool2} {bool2} {bool2 and bool2}")
print(f"{bool2} {bool1} {bool2 and bool1}")
print(f"{bool1} {bool2} {bool1 and bool2}")
print(f"{bool1} {bool1} {bool1 and bool1}")
print("*************************************")
print("Truth table of not operator ")
print(f"{bool2}  {not bool2}")
print(f"{bool1} { not bool1}")
