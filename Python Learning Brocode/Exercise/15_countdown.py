import time


# time.sleep(3)
# print("Times up!")

usertime = int(input("Enter time in seconds"))

for i in range (usertime, 0 ,-1):
    seconds =i%60
    minute= int(i/60)  %60
    hour = int(i/3600)
    print(f"\r{hour}:{minute:02}:{seconds:02}",end="")
    time.sleep(1)
print("\nTimes up!")



'''
#Carriage Return (\r):
# This moves the cursor back to the start of the current line without creating a new line, allowing you to overwrite the previous output on that line.


#end ="":
By default, the print function adds a newline character (\n) after printing, which moves the cursor to the next line. To prevent this, we set end="", which tells the print function not to add a newline after printing the countdown. This ensures the countdown overwrites the same line.


'''