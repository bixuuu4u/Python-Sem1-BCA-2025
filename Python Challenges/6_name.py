#  Write a program that will ask you to enter your name, through keyboard, and perform
# following operations
#  a. Find the middle name
#  b. Find the last name (using string slicing)
#  c. Re-write the name with surname first.

# Taking full name as input
full_name = input("Enter your full name (First Middle Last): ").strip()

# Splitting the name into parts
name_parts = full_name.split()

# Finding the middle name
if len(name_parts) == 3:
    middle_name = name_parts[1]
    last_name = name_parts[2]
    print("Middle Name:", middle_name)
    print("Last Name:", last_name)

    # Rewriting the name with surname first
    new_name = f"{last_name} {name_parts[0]} {middle_name}"
    print("Rewritten Name (Surname First):", new_name)

elif len(name_parts) == 2:
    last_name = name_parts[1]
    print("No Middle Name Found!")
    print("Last Name:", last_name)

    # Rewriting name with surname first
    new_name = f"{last_name} {name_parts[0]}"
    print("Rewritten Name (Surname First):", new_name)

else:
    print("Invalid input! Please enter First, Middle, and Last name properly.")
