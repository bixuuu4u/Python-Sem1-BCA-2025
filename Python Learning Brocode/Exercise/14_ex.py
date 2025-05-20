#Create a strong password
#Pass lenght should be above 8
# Using lowecase upper case and symbols and numbers

user_input = input("Enter a password ::")


has_lenght= len(user_input) >=8
# print(has_lenght)
has_lowecase=False
has_uppercase=False
has_digit=False
has_specialsymbol=False

for char in user_input:
    if char.islower():
        has_lowercase=True
    elif char.isupper():
        has_uppercase=True
    elif char.isdigit():
        has_digit=True
    elif char in "!@#$%^&*?:;'\\-*/+":
        has_specialsymbol=True

if has_lenght and has_lowercase and has_uppercase and has_digit and has_specialsymbol:
    print(f"{user_input}\n This password is strong !!")
else:
    print(f"{user_input} Weak password !!")


if not has_lenght:
    print("\tMust be greater than 8")
if not has_digit:
    print("\tMust contain digit")
if not has_uppercase:
    print("\tMust contain uppercase")
if not has_lowercase:
    print("\tMust contain lowercase")
if not has_specialsymbol:
    print("\tMust contain specialsymbol")