#Global and local variables difference:
#A variable is defined inside and outside the function is called global and local variables.
#A variable is defined outside the function and is accessible to the entire global space is called global variable.
#A variable is defined inside the function is called local variable.
#first case of global variable
'''a=4
def check():
    print("insdie value is",a)
check()
print("outside value is",a)'''

#second case of global variable
'''a=5
def check1():
    a=10
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#third case of global variable
'''a=3
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b+=a
    print("b value is",b)
check2()
print("outside value is",a)
print("outside value of b is",b)'''#error (we don't declare b value at outside the function)

'''a=3
b=2
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b+=a
    print("b value is",b)
check2()
print("outside value is",a)
print("outside value of b is",b)'''

#usage of global keyword
#when user wants to create a variable inside the function directly and carry forward the updated value even outside the function then we need to use global keyword.
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    b=13
    b+=a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''

#ASCII
#chr,ord
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z"))
print(ord(98))#error
print(chr("a"))'''#error

'''for i in range(65,91):
    print(chr(i),end=" ")'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''a=input()
for i in a:
    print(i,"-",ord(i))'''









