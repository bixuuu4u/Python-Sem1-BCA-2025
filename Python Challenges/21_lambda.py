# Program to Demonstrate Lambda Functions, map(), filter(), and reduce()

from functools import reduce

# Lambda function for square of a number
square = lambda x: x**2
print("Square of 5:", square(5))

# Using map() to square each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squares of numbers:", squared_numbers)

# Using filter() to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Using reduce() to find the product of all numbers in a list
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
