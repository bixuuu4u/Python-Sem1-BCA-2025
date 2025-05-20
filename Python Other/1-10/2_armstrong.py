num=int(input("Please,Enter a number: "))
sum=0
copy=num
length = len(str(num))
copy=num
while copy>0:
  power=1
  digit =copy%10
  for i in range (length):
    power *= digit
  sum+=power 
  copy=copy//10

if sum==num:
  print("Armstrong")
else:
  print("Not Armstrong")


  