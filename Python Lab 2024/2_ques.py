#Fahrinte to Centigrade and vice versa

a=int(input("Celcius to fahrinte : 1 dabayen \nFAhrinte to Celcius : 2 dabayen\n\n"))
if(a==1):
    c=int(input("Enter reading in celcius: "))
    print("%d celcius in fahrinte is %d "%(c,c*(9/5)+32))
elif(a==2):
    f =int(input("Enter reading in fahrainte: "))
    print("%d fahranite in celcius is %d "%(f,(f-32)*5/9))
else:
    print("Invalid input")