num=int(input("Please,Enter a number: "))
sum=0
copy=num
length = len(str(copy))
while copy>0:
  sum+=(copy%10) ** length
  copy=copy//10

if sum==num:
  print("Armstrong")
else:
  print("Not Armstrong")


  