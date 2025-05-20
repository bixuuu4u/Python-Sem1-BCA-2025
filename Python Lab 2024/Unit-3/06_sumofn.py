# Write a function that accepts variable-length arguments (*args) and returns their sum.

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5,6))