num=int(input("Please,Enter a number: "))
sum=0
copy=num
total_digits=0
while copy!=0:
  copy=copy//10
  total_digits+=1
copy=num
while copy>0:
  power=1
  digit =copy%10
  for i in range (total_digits):
    power *= digit
  sum+=power 
  copy=copy//10

if sum==num:
  print("Armstrong")
else:
  print("Not Armstrong")


  