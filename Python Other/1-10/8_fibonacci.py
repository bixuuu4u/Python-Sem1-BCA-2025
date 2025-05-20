num=int(input("Enter number: "))
x=0
y=1
if num>0:
  print(f"{x}",end=" ")
if num>1:
  print(f"{y}",end=" ")
for i in range(2,num):
  temp =x+y
  print(f"{temp}",end=" ")
  x=y
  y=temp