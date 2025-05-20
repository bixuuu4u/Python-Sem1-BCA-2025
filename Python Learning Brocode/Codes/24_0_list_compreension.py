#List comprehension = a concise way to create lists in python
#       Compact and easier to read than traditional loops
#       [Expression for value in itreable if condition]

'''doubles=[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)'''


doubles=[x*2 for x in range(1,11) ]
print(doubles)
triples=[y*3 for y in range(1,11) ]
print(triples)
square=[z*z for z in range(1,11) ]
print(square)