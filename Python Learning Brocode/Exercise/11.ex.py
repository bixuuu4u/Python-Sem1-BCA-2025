#Weight Convertor

weight =float(input("Enter your weight :"))

user_choice=input("Kilograms or Pound [K/P] :").upper()
# print(user_choice.lower())

if user_choice =="K":
    weight = weight * 2.205
    user_choice = "Lbs."
    print(f"Your weight is :{round(weight,3)}{user_choice}")
elif user_choice =="P":
    weight = weight / 2.205
    user_choice ="Kgs."
    print(f"Your weight is :{round(weight,3)}{user_choice}")

else:
    print(f"{user_choice} is not valid !!")