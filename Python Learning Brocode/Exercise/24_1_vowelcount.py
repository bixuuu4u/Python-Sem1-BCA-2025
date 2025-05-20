user_input=input("Enter a sentence or name.. etc :")

count_vowel=0
count_consonant=0

vowels='aeiou'

for i in user_input.lower():
	if i in vowels:
		count_vowel+=1
	elif i ==' ':
		continue
	else:
		count_consonant+=1



print(f"Vowels: {count_vowel}|Consonant: {count_consonant}")