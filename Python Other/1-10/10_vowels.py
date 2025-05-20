text=input("Enter a text: ")
vowel=0
for char in text:
  if char in "aeiou":
    vowel+=1
print(f"Vowels in {text}:{vowel}")