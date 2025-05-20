#Default arguments - A default value for certain parameters
#                    default is usedwhen that argument is omitted
#                   make your function more flexible,reduces no of arguments
#                   1.Positional,2.DEFAULT,3.Keyword ,4.Arbitary


# def net_price(list_price,discount,tax):
#     return list_price*(1-discount)*(1+tax)

# print(net_price(500,0,0.05))
#Now lets imagine that the discount in most of the cases is 0 and the tax is almost same
#so set the parameters a default value 
def net_price(list_price,discount=0,tax=0.05):
    return list_price*(1-discount)*(1+tax)
print(net_price(500,0,0.05)) 
print(net_price(500,0.1)) 
print(net_price(500,0.1,0)) 