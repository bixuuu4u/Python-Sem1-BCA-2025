#COnditional OPerator -- One line shortcut for if-else
#                Print or assign one of the values based on the conditon 
#                X if condition else Y

num=1
num2=8

print("Positive" if num>0 else "Negative")

print("Even" if num%2==0 else "Odd")



max= num if num> num2 else num2
print("Max is %d"%max)



min= num if num< num2 else num2
print("Min is %d"%min)