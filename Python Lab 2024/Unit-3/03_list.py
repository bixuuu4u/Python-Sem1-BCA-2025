# Write a function that takes a list of numbers and returns the sum of all even numbers.
def sum_even(list):
    return sum(x for x in list if x%2==0)

print(sum_even([1,2,3,4,5,6]))