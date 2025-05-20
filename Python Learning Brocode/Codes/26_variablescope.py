#variable Scope +where a variable is visible and accessible
#Scope resolution(LEGB) Local-> Enclosed -> Global ->  Built-in

def fun_1():
    a=1#local to function 1
    print(a)
    # print(b) Name error b is not defined
    x =8
    print(x)

def fun_2():
    b=2#local to function 2
    print(b)
    x =9
    print(x)

fun_1()
fun_2()