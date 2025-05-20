# *args - allows you to pass multiple non-key arguments
# **kwargs - allows you to pass multiple keyword-arguments
#                    * unpacking operator
#                     1.Positional 2.deafult 3.keyword 4.ARBITARY


def add(*args):
    total=0
    for arg in args:
        total +=arg
    return total


print(add(1,2,3,5,6,7,8,9 ))
