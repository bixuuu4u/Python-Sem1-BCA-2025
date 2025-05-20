def sumofdigits(num):
  sum=0
  while num!=0:
    sum+=num%10
    num=num//10
  return sum

n=int(input("Enter a number: "))

print(f"Sum of Digits {sumofdigits(n)}")