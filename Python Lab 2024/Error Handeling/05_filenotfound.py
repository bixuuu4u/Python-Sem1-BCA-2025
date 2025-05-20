try:
    f1=open("C:\\Users\\biswa\\Desktop\\Python Lab\\Error Handeling\\xyz.txt","r")
    #f1.read()
    print(f1.read())
except:
    print("File not found")

    