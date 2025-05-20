#A quiz gaem using tuple  2d tuple for options


questions = (
    "What is the SI unit of force?",
    "Which of the following is the formula for gravitational force?",
    "The center of mass of a uniform ring lies?",
    "The formula for the kinetic energy of an object is?",
    "Which of the following is a vector quantity?"
)

options = (
    ("A. Newton", "B. Joule", "C. Pascal", "D. Watt"),
    ("A. F = ma", "B. F = G(m1 * m2) / r^2", "C. F = kq1q2 / r^2", "D. F = mv^2"),
    ("A. At the center of the ring", "B. At the edge of the ring", "C. At a point outside the ring", "D. At the point of contact with the surface"),
    ("A. KE = 1/2mv", "B. KE = mv^2", "C. KE = 1/2mv^2", "D. KE = mv"),
    ("A. Distance", "B. Speed", "C. Displacement", "D. Time")
)





answers=("A","B","A","C","C")   # "a", "b", "a", "c", "c"

guesses=[]

score=0

question_number =0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess=input("Enter the correct answer[A,B,C,D] : ").upper()
    checkforguess = guess.isalpha() 
    if checkforguess:
        # print("done")
        guesses.append(guess)
    if guess ==answers[question_number]:
        score+=1
        print("CORRECT !")
    else:
        print("INCORRECT !")
        print(f"{answers[question_number] } is correct")
    question_number+=1
print("--------------------------------")
print("            RESULTS             ")
print("--------------------------------")
print("Answers :",end="")
for answer in answers:
    print(answer,end=" ")
print()
print("Your Answer :",end="")
for guess in guesses:
    print(guess,end=" ")


score = int(score/len(questions) *100)
print(f"Your score is {score}%")