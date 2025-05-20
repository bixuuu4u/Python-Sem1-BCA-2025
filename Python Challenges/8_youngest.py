#  Find out the youngest among Shyam, Dugu and Ishan whose ages are entered by the
# user through keyboard.

# Taking input from the user
shyam_age = int(input("Enter Shyam's age: "))
dugu_age = int(input("Enter Dugu's age: "))
ishan_age = int(input("Enter Ishan's age: "))

# Finding the youngest
if shyam_age < dugu_age and shyam_age < ishan_age:
    print("Shyam is the youngest.")
elif dugu_age < shyam_age and dugu_age < ishan_age:
    print("Dugu is the youngest.")
elif ishan_age < shyam_age and ishan_age < dugu_age:
    print("Ishan is the youngest.")
else:
    print("There is a tie.")
