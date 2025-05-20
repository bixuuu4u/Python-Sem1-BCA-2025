text=input("Enter a text: ")
'''
if text==text[::-1]:
  print(f"{text} is palindrome")
else:
  print(f"{text} is not palindrome")
'''

length =len(text)

for i in range (length):
  if (text[i]!= text[length-1-i]):
    print(f"{text} is not palindrome")
    break
else:
  print(f"{text} is palindrome")
