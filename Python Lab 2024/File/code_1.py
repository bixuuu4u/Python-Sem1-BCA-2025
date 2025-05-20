f1=open("C:\\Users\\biswa\\Desktop\\Python Lab\\File\\source.txt","r")
f2=open("C:\\Users\\biswa\\Desktop\\Python Lab\\File\\destination.txt","w")
data=f1.read()

# for i in data:
    # print(f2.write(i))


f2.write(data)  #Efficient


f1.close()
f2.close() 