#Format speciiers = {value:flags} fprmat a value based on what flags are inserted


# .(number)f -round to that many deciml places (fixed  point)
# :(number) = allocate that many spaces
#:03 allocate and zero pad that many spaces
# :< left justify
#:> right justify
# :^ center align
# :+ use a + sign to indicate positive value
# := place a sign to leftmost position
# :  = insert space before positibve numbers
# :, comma separater 
# Mixed Combinations can be done also


num= 3.21342
num2=-322.32
num3=23.211
# print(num)
print("--------------------------")

print(f"Number 1 is {num:.2f}")
print(f"Number 2 is {num2:.2f}")
print(f"Number 3 is {num3:.2f}")
print("--------------------------")
print(f"Number 1 is {num:10}")
print(f"Number 2 is {num2:10}")
print(f"Number 3 is {num3:10}")
print("--------------------------")
print(f"Number 1 is {num:010}")
print(f"Number 2 is {num2:010}")
print(f"Number 3 is {num3:010}")
print("--------------------------")
print(f"Number 1 is {num:<}")
print(f"Number 2 is {num2:<}")
print(f"Number 3 is {num3:<}")
print("--------------------------")
print(f"Number 1 is {num:>}")
print(f"Number 2 is {num2:>}")
print(f"Number 3 is {num3:>}")
print("--------------------------")
print(f"Number 1 is {num:^}")
print(f"Number 2 is {num2:^}")
print(f"Number 3 is {num3:^}")
print("--------------------------")
print(f"Number 1 is {num:+}")
print(f"Number 2 is {num2:+}")
print(f"Number 3 is {num3:+}")
print("--------------------------")

