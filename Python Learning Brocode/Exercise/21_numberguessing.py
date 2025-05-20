#Number GUessing game

import random

difficulty = int(input("Enter difficulty [10,Easy][100,Mid][500,Hard]: "))

random_number = random.randint(0,difficulty)
guesses=0
while True:
    user_guess= input("Guess the number")

    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess>random_number:
            print("LOWER")
        if user_guess<random_number:
            print("HIGHER")
        if user_guess== random_number:
            break
        if user_guess< 0 or user_guess> difficulty:
            print("Guess is out of range")
            guesses-=1
        guesses+=1
    else:
        print("Invalid input")
        print(f"Guess a number betn {0} and {difficulty}")
print(f"You gussed it right in {guesses} attemmpts", )