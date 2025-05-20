import time 
def countdown(end,start=0):#have to reverse if use non default arguments
    for i in range(end,start,-1):
        print(i)
        time.sleep(1)
    print("Times up !")

countdown(10,5)