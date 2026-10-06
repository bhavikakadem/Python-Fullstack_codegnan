#Functions
#A function is a block of organized, re-usable code and that is used to perform a single or multiple tasks.
#Python gives in-built functions like print
#function blocks begin with the keyword def, followed by the function name and paranthesis()
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the integer division is:",a//b)
    print("the power is:",a**b)
    print("the modulo division is:",a%b)
calculate(10,5)
calculate(4,4)
calculate(10,2)'''

'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''

'''while True:
def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()#function calls itself
add()'''

'''def fullname():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
fullname()'''

#print- it just shows the human user output in a console.
#return- it is used to terminate the function and gives back a value from the function.

'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
mul(5,2)'''# it doesn't display anything becasue here we are using return not print function.

'''def mul(a,b):
    return a*b
print(mul(5,2))'''

#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(5,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(cal(5,4))'''#it will only displays the first return value by using print function, remaining return statements are skippied

'''def cal():
    a=int(input("Enter a value"))
    b=int(input("Enter b value"))
    option=int(input("select (1/2/3)"))
    if(option==1):
        print(a+b)
    elif(option==2):
        print(a-b)
    else:
        print(a*b)
    cal()
cal()'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
        a=int(input("Enter a value"))
        b=int(input("Enter b value"))
        option=int(input(choose the option
                         1. add
                         2. sub
                         3. mul))
        if option==1:
            add()
        elif option==2:
            sub()
        elif option==3:
            mul()'''

'''def bill():
    persons=int(input("Enter no. of persons:"))
    amount=int(input("Enter amount:"))
    print("Amount per head:",(amount//persons))
bill()'''

'''def bill():
    persons=int(input("Enter no. of persons:"))
    amount=int(input("Enter amount:"))
    print(f" Amount per head: {amount//persons}")
bill()'''

'''def bill():
    persons=int(input("Enter no. of persons:"))
    amount=int(input("Enter amount:"))
    print("Amount per head:{}".format(amount//persons))
bill()'''

#Keywords and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="Bhavika"
    mailid="bhavika@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="Bhavika",mailid="bhavika@gmail.com")
Details(id=30,name="sailaja",mailid="sailu@gmail.com")
Details(40,"varshitha","varshi@gmail.com")
Details("Deepu","deepu@gmail.com",4)
Details(mailid="chitti@gmail.com",name="Mahi",id=6)'''

#employee-name,salary,designation
'''def employee(name,salary,designation):
    print(name,salary,designation)
employee(name="name",salary="salary",designation="designation")
employee(name="Mahi",salary=100000,designation="DBA")
employee(name="Sai",salary=50000,designation="QA")
employee(name="Sanjay",salary=80000,designation="DA")
employee(name="Abbas",salary=70000,designation="Java Developer")
employee("chandu",60000,"Teacher")
employee(50000,"sailu","QA")
employee(designation="cricketer",name="Rohit",salary=100000)'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1800)'''

'''def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="sugar",price):
#always first parameter should be null or both or we have to pass both the parameters
#non-default arg follows default argument
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

#bakery-cake,price,quantity
'''def bakery(cake,price,quantity):
    print("cake is %s"%cake)
    print("price is%d"%price)
    print("quantity is %s"%quantity)
bakery("pineapple",700,"1kg")'''

'''def bakery(cake="strawberry",price=1200,quantity="2kg"):
    print("cake is %s"%cake)
    print("price is%d"%price)
    print("quantity is %s"%quantity)
bakery()'''

'''def bakery(cake,price=800,quantity="1kg"):
    print("cake is %s"%cake)
    print("price is%d"%price)
    print("quantity is %s"%quantity)
bakery("Black Forest")'''

'''def bakery(cake,price,quantity="2kg"):
    print("cake is %s"%cake)
    print("price is%d"%price)
    print("quantity is %s"%quantity)
bakery("chocolate",700)'''

# *arguments - * is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''b=(5,6,7,8,9)
print(b)
print(*b)'''

'''c={2,3,4,6,7,8}
print(c)
print(*c)'''

'''d={"name":"Bhavika","year":2005}
print(d)
print(*d)'''

'''e="codegnan"
print(e)
print(*e)'''

'''a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''#error

'''a,*b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9
print(a)
print(*a)
print(b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

#variable length arguments-variable length arguments are automatically stores in tuple and we use *arguments.
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[4,5,6,7,8,9]
check(*b)
c=(3,4,5,6)
check(*c)
d={6,7,8,9}
check(*d)
e={"year":2005,"month":"jan"}
check(*e)'''

'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        d+=i
        print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,3.4,4.2,5.3)
check1(3,4,5,2,3.2,4.4,"Pooja")'''#error

'''def check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) is int or type(i) is float: #type(i) in (int,float)
            d+=i
            print(d)
check1()
check1(3,4,5,2,3.2,4.4,"Pooja")'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["mahesh","shanavaz","nivas"],
   "marks":[20,30,40],
   "status":["p","a","p"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["mahesh","shanavaz","nivas"],
   "marks":[20,30,40],
   "status":["p","a","p"]}
details(**d)'''

#both * and **
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d+=i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,3.4,5.2)
final(*data)
details={"names":["bhavika","priya","sowmya"],
         "marks":[60,70,80]}
final(**details)
final(*data,**details)'''






    
    
    
    



    
    
