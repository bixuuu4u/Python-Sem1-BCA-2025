foods = input("Enter foods you like[q to quit]: ")

while not foods =="q":
    print(f"You like {foods}")
    foods = input("Enter someother foods you like[q to quit]: ")

print("Bye")

num = int(input("Enter a number [1 - 10]:"))

while num<1 or num>10:
    print(f"{num} is not valid")
    num = int(input("Enter a number [1 - 10]:"))
print(f"Your num is {num}")

