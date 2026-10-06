#Conditions
'''1. if
2. elif
3. else
Another
1. if
2. if-else
3. if elif-else
4. multiple if
5. multiple elif
6. Nested-if'''
#if-condition by using comparision operators
#<,>,<=,>=,==,!=
'''a=10
b=20
if (a<b):
    print("True")'''

'''a=40
b=60
if (a>b):
    print("Greater")'''

'''a=50
b=80
if(a<=b):
    print("Lessthan")'''

'''a=89
b=10
if(b!=a):
    print("Not Equal")'''

'''a=20
b=20
if(a==20):
    print("Equal")'''

'''a=30
b=90
if(b>=a):
    print("Greaterthan")'''

'''a="Python"
if(a=="Python"):
    print("True")'''

'''a=int(input())
b=int(input())
if(a==b):
    print("True")'''

'''a=int(input())
if (a>=20):
    print("True")'''

#if-condition by using logical operators
#and,or,not
'''a=4
b=8
if a<b and b>a:
    print("True")'''

'''a=6
b=9
if a<=b and b>=a:
    print("treu")'''

'''a=7
b=10
if a!=b and b==a:
    print("False")'''

'''a=10
b=20
if a<b or b<a:
    print("True")'''

'''a=30
b=40
if(a>=b or b<=a):
    print("True")'''

'''a=40
b=10
if(a!=b or a==b):
    print("Not Equal")'''

'''a=20
b=90
if not a>b:
    print("Not Greaterthan")'''

'''a=29
b=20
if not a<b and b!=a:
    print("True")'''

'''a=int(input())
b=int(input())
if not a==b or a<b:
    print("false")'''

#if-condition by using identify operators
#is,is not
'''a=10
if type(a) is int:
    print("True")'''

'''a=20
b=30
if type(a) is not int:
   print("True")'''

'''a=10
b=50
if type(a) is float:
    print("True")'''

'''a=int(input())
b=int(input())
if( type(a) is int and type(b) is float):
    print("True")'''
   
'''a=int(input())
b=float(input())
if( type(a) is int and type(b) is float):
    print("True") '''

'''a=int(input())
b=int(input())
if( type(a) is int and type(b) is not float):
    print("True")'''

#if-condition by using membership operators
#in,not in
'''a=[2,3,4,5,6,7,8,9]
if 5 in a:
    print("True")'''

'''a=[2,3,4,5,6,7,8,9]
if 10 not in a:
    print("True")'''

'''a=[2,3,4,5,6,7,8,9]
if 15 in a:
    print("True")'''

'''a=int(input())
if 30 in a:
    print("True")#error'''

'''a=[2,3,4,5,6,7,8,9]
b=int(input())
if(b in a):
    print("True")'''

#if-else conditions by using comparision operators
'''a=5
b=10
if a<b:
    print("TRUE")
else:
    print("FALSE")'''

'''a=5
b=30
if(a>b):
    print("TRUE")
else:
    print("FALSE")'''

'''a=40
b=10
if(a!=b):
    print("TRUE")
else:
    print("FALSE")'''

'''a=40
b=20
if(a==b or a>b):
    print("TRUE")
else:
    print("FALSE")'''

'''a=30
b=10
if(a<=b and b>a):
    print("True")
else:
    print("False")'''

'''a=[2,3,4,5,6,7,8,9]
if(10 in a):
    print("YES")
else:
    print("NO")'''

'''a=[1,2,3,4,5,6,7,8,9]
if(10 not in a):
    print("YES")
else:
    print("NO")'''

'''a=int(input())
if(type(a) is int):
    print("YES")
else:
    print("NO")'''

'''a=float(input())
if(type(a) is not int):
    print("NO")
else:
    print("YES")'''

#if-elif-else conditions by using comparision operator
'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=5
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=10
b=20
if(a==b):
    print("Equal")
elif (b<a):
    print("less")
elif (a!=b):
    print("Not Equal")
else:
    print("true")'''

'''a=10
b=20
if(a<b and b!=a):
    print("not equal")
elif(a>b or a==b):
    print("Equal")
else:
    print("less or greater")'''

'''a=30
b=40
if(type(a) is int):
    print("true")
elif(type(a) is not int):
    print("false")
else:
    print("datatype")'''

'''a=[1,2,3,4,5,6,7,8,9]
b=20
if(b in a):
    print("YES")
elif(b not in a):
    print("NO")
else:
    print("either")'''

#multiple-if
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''


'''a=5
b=10
if a==b:
    print("Equal")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''


'''a=5
b=10
if a<b and a!=b:
    print("true")
if b>a or a!=b:
    print("greater")
if a!=b:
    print("not equal")'''


'''a=5
b=10
if type(a) is int:
    print("yes")
if type(a) is not int:
    print("No")'''

'''a=[10,20,40,30,50,60,70,80,90]
b=30
if(b in a):
    print("true")
if(b not in a):
    print("false")'''

#nested-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

'''a=40
b=30
if a!=b:
    print("Not equal")
    if type(a) is int:
        print("Integer")
    else:
        print("not an integer")
else:
    print("equal")'''

'''a=30
b=20
if a!=b and a>b:
    print("Not equal")
    if(type(a) is not int):
        print("not an integer")
    else:
        print("integer")
else:
    print("Equal")'''

'''a=[1,2,3,4,5,6,7,8,9]
b=50
c=2
if b not in a or c in a:
    print("less")
else:
    print("greater")'''































