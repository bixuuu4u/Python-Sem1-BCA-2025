def armstrong(x):
    s=len("x")
    print(type(s))
    result=1
    remainder=0
    while x>0:
        remainder=x%10
        result=result+remainder**s
        x=x/10
    if x==result:
        return True

print(armstrong(122))