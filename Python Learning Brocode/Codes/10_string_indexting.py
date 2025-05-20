#Indexing -- accessing elements of a sequence using [] -> indexing operator
#       [start : end : step]  ending index is exclusive (n-1)

number ="1313-24454-24353-532453"
print(len(number))
print(number[1])


print(number[0:4])
# print(number[:4])

print(number[5:9])


print(number[5:])

#Negegtive index     last char is -1

print(number[-1])
print(number[::2]) #Step


last4number =number[-4:]
print(last4number)


# Negetive 1 step would reverse a string

revnumber = number[::-1]
print(revnumber)