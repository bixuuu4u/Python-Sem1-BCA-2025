numbers=[1,-2,3,-4,5,-6,8]

positive_num=[number for number in numbers if number>=0]
print(positive_num)
negetive_num=[number for number in numbers if number<0]
print(negetive_num)

even_num =[number for number in numbers if number%2==0]
print(even_num)
odd_num =[number for number in numbers if number%2!=0]
print(odd_num)