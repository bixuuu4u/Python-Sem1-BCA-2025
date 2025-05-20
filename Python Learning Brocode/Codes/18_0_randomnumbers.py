import random

# print(help(random))


dice=random.randint(1,6)  #dice
print(dice)


low=0
high=20
dice=random.randint(low,high)
print(dice)

floating =random.random()
print(floating)
options =("Rock","Paper","Sessoiors")
randomchoice =random.choice(options)
print(randomchoice)
print(options)
list =["1","2","3","4","5","6","7","8","9"]
random.shuffle(list)
print(list)