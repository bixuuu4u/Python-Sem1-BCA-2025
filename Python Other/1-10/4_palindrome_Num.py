num=int(input("Enter a number: "))
rev=0

copy=num
while copy!=0:
  rev=rev*10+copy%10
  copy=copy//10
if num==rev:
  print(f"{num} is armstrong")
else:
  print(f"{num} is not armstrong")
