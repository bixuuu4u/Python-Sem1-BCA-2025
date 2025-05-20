num_pad1=(1,2,3)
num_pad2=(4,5,6)
num_pad3=(7,8,9)
num_pad4=("*",0,"#")
num_pad=(num_pad1,num_pad2,num_pad3,num_pad4)

# print(num_pad)

for i in num_pad:
    for num in i:
        print(num,end=" ")
    print()