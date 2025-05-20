#Print a rectangle or squre with some symbol using rows and colm of user

row = int(input("Enter Row size :"))
col = int(input("Enter Col size :"))
symbol=input("Enter a symbol :")
#sq 
for i in range(row):
    for j in range(col):
        print(f"{symbol}",end="")
    print("")

#rectangle
for i in range(row):
    for j in range(col):
        print(f"{symbol} ",end="")
    print("")