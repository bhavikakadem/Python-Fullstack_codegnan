#Built-in functions

#fromkeys()-is used to convert a string into dictionary
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))#error
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"bhavika")#if we want to give values to the keys
print(c)
c["g"]="python"#if we want to give value to a specific key
print(c)'''

#eval()-is used in runtime to take any type of data irrespective of the datatype.
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()-used to combine multiple collections into single collection
'''a=[10,20,30,40,50]
names=["Bhavika","sailaja","Nousheen","srividya","bindu"]
print(a+names)
b=zip(a,names)#binary format
print(b)
c=list(zip(a,names))#if we want to make a collection then we need to use datatype.
print(c)
d=tuple(zip(a,names))
print(d)
e=set(zip(a,names))
print(e)
f=dict(zip(a,names))
print(f)'''

#enumerate()-we can give counter to the collection
'''names=["Bhavika","sailaja","Nousheen","srividya","bindu"]'''
'''for i in range(len(names)):
    print(i,names[i])'''

'''b=list(enumerate(names))
print(b)

c=list(enumerate(names,10))#if we want count from a specific number
print(c)'''

'''d=tuple(enumerate(names))
print(d)'''

'''e=set(enumerate(names))
print(e)'''

'''f=dict(enumerate(names))
print(f)'''

#annonymous functions- are nameless functions and we use a keyword called as lambda to create annonymous functions.

'''def cal():
    a=2*x+5
    print("value for the expression:",a)
x=int(input())
cal()'''

'''def cal(x):
    a=2*x+5
    print("value for the expression:",a)
cal(5)'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x*y
print(a(2,2))'''

'''a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

'''a="python"
b=lambda a:a.upper()
print(b(a))'''

'''a=input()
b=input()
c=lambda a,b:a+" "+b
print(c(a,b))'''

'''a,b=[str(x) for x in input("enter the values").split(",")]
c=lambda a,b:a+" "+b
print(c(a,b))'''

#filter()
'''a=[2,6,7,9,10,12,15,20,40,55,60,80]'''
'''if a%2==0::
    print(a)#error'''

'''for i in a:
   if i%2==0:
       print(i)'''

'''b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[[],(),set(),{}," ",None,3,8.8,"python",8+2j,True,False]
b=list(filter(None,a))
print(b)
print(type(b))
for i in a:
    print(type(i))
for i in b:
    print(type(i))'''

#map()-each object from a collection and forms a new collection
'''a=[2,4,6,8,9,10,12,15,20,25]
b=[1,5,3,0,4,20,25,30,60,80]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

#run_time input()
'''a=int(input("a value:"))
b=int(input("b value:"))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b)'''#error

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=[x for x in input("Data").split(",")]
print(a+b)'''

'''a,b=input("data").split(",")
print(a+b)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=list(map(int,input("data").split(",")))
print(a)'''

'''a=list(map(str,input("data").split(",")))
print(a)'''

'''a=tuple(map(str,input("data").split(",")))
print(a)'''

'''a=tuple(map(int,input("data").split(",")))
print(a)'''

'''a=set(map(int,input("data").split(",")))
print(a)'''

'''a=list(map(eval,input("data").split(",")))
print(a)'''

'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''


















