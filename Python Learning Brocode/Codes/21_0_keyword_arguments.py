#Keyword arguments - An argument spreceded by an identifiers
#                     Help with readability
#                     order of arguments doesnot  matter
#                     1.Positional 2.deafult 3.KEYWORD 4.Arbitary



def hello(greeting,title,first,last):
    print(f"{greeting } {title}{first} {last}")

hello("Hello","Mr.","Biswajeet","Sahoo")
hello("Hello","Biswajeet","Sahoo","Mr.")
hello(greeting="Hello",first="Biswajeet",last="Sahoo",title="Mr.")


for x in range(1,11):
    print(x,end=" ")  #this end is a keyword aargument of print function
print()
print("1","2","3","4",sep="-") 