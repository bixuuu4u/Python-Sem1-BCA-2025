#Rock Paper Secissors
import random
options =("Rock","Paper","Scissors")
# print(computer_choice)
user_choice=None
user_score=0
computer_score=0
is_playing=True
print("Rock Paper Scissors Python Game")

while is_playing:
    user_choice=input("\tMake your choice  \n\t[1 .Rock]\n\t[2 . Paper]\n\t[3 . Scissor]\n\t[q to quit]").capitalize()
    #Exit Loop
    if user_choice=="Q":
        print("Thanks for playing! ")
        print(f"-----Scores-----\nPlayer:{user_score}:|:Computer:{computer_score}")
        is_playing=False
    if user_choice =="1":
        user_choice="Rock"
    if user_choice =="2":
        user_choice="Paper"
    if user_choice =="3":
        user_choice="Scissors"
    # print(user_choice) 
    if user_choice not in options: 
        print("Invalid Choice")
        continue
    computer_choice =random.choice(options)
    print(f"Player-{user_choice}:|:Compunter-{computer_choice}")
    if user_choice==computer_choice:
        print("IT S A TIE")
    elif user_choice =="Rock" and computer_choice== "Scissors":
        print("You win")
        user_score+=1
    elif user_choice =="Paper" and computer_choice== "Rock":
        print("You win")
        user_score+=1
    elif user_choice =="Scissors" and computer_choice== "Paper":
        print("You win")
        user_score+=1
    else:
        print("You lose!!")
        computer_score+=1