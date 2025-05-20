# input()  A function that  prompts the usr to enter data 
#                 Returns the data as string 

# input() need a prompt so that the user undertsant what to do



user_name =input("Enter your name : ")
user_age =input("How old are you: ")
user_age=int(user_age)
print(f"Heyy {user_name}")
print(f"You are  {user_age} years old")  #Add 1 to age
user_age +=1  #type errror 
print("Happy Birthday")