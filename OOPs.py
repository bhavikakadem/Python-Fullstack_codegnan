#OOPs
'''1. A class contains attributes, variables and methods or functions that can manipulate the data.
2. A class is the blue print of an object.
3. An object is an initiation of a class.
4. Methods are functions that define inside the body of the class.
# 4- pillars of oops
1. Polymorphism - In this we have 4 types.  They are
 -operator overloading
 -operator overriding
 -method overloading
 -method overriding
2. Inheritance - In this we have 5 types.  They are
 -single inheritance
 -multiple inheritance
 -multi level inheritance
 -hybrid inheritance
 -hierarical inheritance
 also we have super() function.
3. Encapsulation - In this we have 3 types.  They are
 public data
 __private-data
 _protected-data
4. Abstraction - In this we have,
 -abstract calss
 -abstract method'''

#syntax
'''class classname():
    #attributes
    name="Bhavika"
    age=21
    city="Guntur"
    def fname(method_name):
        print(statements....)
a=classname()
a.fname()'''

#class declaration
'''class Details():
    name="Bhavika"
    age=21
    city="Guntur"
    def display(self):
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("Bhavika",21,"Guntur")
a.display()
a.data("Varshitha",21,"Guntur")
a.display()
a.data("Deepu",13,"Guntur")
a.display()
b=Details()
b.data("Sailaja",23,"Guntur")
b.display()'''

#object initialization
#__init__
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("Bhavika",21,"Guntur")
print(dir(a))
a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(name=input(),age=int(input()),place=input())
print(dir(a))
a.display()'''
 
'''class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()'''

#diff b/w _ and __
#when user wants to create a variable in python with __ our python interpreter treats it as a special variable and avoid name conflicts with methods and inner classes.
'''class Employee1():
    def __init__(self):
        self.name="Bhavika"
        self._mailid="bhavikakadem"
        self.__salary=50000
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee1__salary)'''

'''class Employee1():
    def __init__(self):
        self.name="Bhavika"
        self._mailid="bhavikakadem"
        self.__salary=50000
class Employee2():
    def __init__(self):
        self.name="Sailaja"
        self._mailid="sailu@gmail.com"
        self.__salary=60000
a=Employee1()
b=Employee2()
print(a._Employee1__salary)
print(b._Employee2__salary)'''

#polymorphism
#1. operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(8))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(4))
print(a.__ge__(10))
print(a.__le__(20))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print("Bhavika".__add__("Kadem"))'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
a=A(10)
b=B(20)
print(a+b)'''

'''class A():
    def __init__(self,a):
        self.a=a
    def __sub__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
a=A(10)
b=B(20)
print(a-b)'''


#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum is:",a+b+c)
        elif a!=None and b!=None:
            print("product is:",a*b)
        else:
            print("program ends....")
a=new()
a.sum()
a.sum(1,2,3)
a.sum(4,5)'''

'''class new():
    def sum(self,a,b,c):
        if a!=None and b!=None and c!=None:
            print("Sum is:",a+b+c)
        elif b!=None and a!=None:
            print("product is:",a*b)
        else:
            print("program ends....")
a=new()
a.sum(1,2,3)
a.sum(None,4,5)'''

#method overriding
'''class Animal():
    def speak(self):
        print("Animal can makes sounds")
class Dog():
    def speak(self):
        print("Dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class A():
    def vehicle(self):
        print("car")
class B():
    def vehicle(self):
        print("Bike")
a=A()
b=B()
a.vehicle()
b.vehicle()'''

#Inheritance
#single-inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#Multiple-inheritance
'''class Father():
    height=5.5
    def info(cls):
        print("Father Info:",cls.height)
class Mother():
    weight=60
    def info1(cls):
        print("Mother Info:",cls.weight)
class kid(Father,Mother):
    dob="10-1-2005"
    def info2(cls):
        cls.info()
        cls.info1()
        print("Kid Info:",cls.dob)
a=kid()
a.info2()
a.info()
a.info1()'''

#Multi-level inheritance
'''class GP():
    land="2 Acres"
    def info(cls):
        print(cls.land,"of land")
class Parent(GP):
    house="1000 sqft"
    def info2(cls):
        cls.info()
        print(cls.house,"house")
class Child(Parent):
    car="Thar"
    def info3(cls):
        cls.info2()
        print(cls.car)
a=Child()
a.info3()'''

#Hierarchical - means one parent class is inherited by multiple child classes.
'''class Employee():
    company="Codegnan"
    def info(cls):
        print(cls.company)
class Trainer(Employee):
    teach="Python"
    def info1(cls):
        cls.info()
        print(cls.teach)
class Developer(Employee):
    code="Frontend"
    def info2(cls):
        cls.info()
        print(cls.code)
a=Developer()
a.info2()
b=Trainer()
b.info1()'''

#Hybrid inheritance - means combining one or more than one type of inheritance. for example-hierarchical+multiple
'''class Trainer():#parent
    teach="Python"
    def info(cls):
        print(cls.teach)
class Developer(Trainer):#child-1
    code="Frontend"
    def info1(cls):
        cls.info()
        print(cls.code)
class Student(Trainer):#child-2
    study="studying"
    def info2(cls):
        cls.info()
        print(cls.study)
class Program_Manager(Student,Developer):
    work="working"
    def info3(cls):
        cls.info2()
        cls.info1()
        print(cls.work)
a=Program_Manager()
a.info3()'''

#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("Parent constructor")
class child(parent):
    def __init__(self,name,city):
        super().__init__(name)
        self.city=city
        print("Child constructor")
a=child("Bhavika","Gnt")
print(a.name)
print(a.city)'''

#Encapsulation-combining multiple units into single unit is known it as a encapsulation.  It encapsulate both methods and data.
#1. public
'''class A():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
x=B()
x.method1()
x.method2()'''
#2. protected
'''class A():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
x=B()
x.method1()
x.method2()'''
#3. private
'''class A():
    __privatedata=100
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
x=B()
x.method1()
x.method2()
print(x._A__privatedata)'''

#Abstraction - hiding unneccessary info from user is called abstraction.
#abstract class - morethan one abstract methods is called abstract class.
#abstract method - a method is declared without implementation is called abstract method.
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data")
obj1=A()
obj1.method()'''#error

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 implementation")
    def method3(self):
        print("method2 implementation")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()



