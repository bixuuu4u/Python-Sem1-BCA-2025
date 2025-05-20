def fibonacci(x,y,num):
  if num==0:
    return
  print(f"{x}",end=" ")

  fibonacci(y,x+y,num-1)


num=int(input("Enter number: "))

fibonacci(0,1,num)