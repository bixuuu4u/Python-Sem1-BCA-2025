#  Create a function that returns the reverse of a string without using slicing.
def reverse_string(str):
    rev=""
    for char in str:
        rev=char+rev
    return rev

print(reverse_string("hello"))    