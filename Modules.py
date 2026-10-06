#diff b/w module, library, and package
#module - a module is a single python file, it consists python code.
#A module contains variables, functions, and classes.
#Examples of modules such as, my_module.py, math.py,random.py
#package - A package contains collection of python modules is known it as package
#examples-requests, numpy, pandas
#library - it consists both modules and packages.
#examples- numpy,pandas,matplotlib,django
#Note:Every python file is a module and import is a keyword.
#every python file is saved internally with variable name as __main__

#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(4))
print(math.pow(2,4))
print(math.log(10))
print(math.cos(60))
print(math.tan(45))
print(math.ceil(3.9))
print(math.ceil(9.12))
print(math.floor(6.5))'''

'''from math import pi,log,sqrt,tan
print(pi,log(2),sqrt(10),tan(45))'''

#sys module
'''import sys
print(sys.path)'''

'''for i in sys.path:
    print(i)'''

'''print(sys.version)'''

#os module
import os
#print(os.path)
#print(os.getcwd())#current path
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("C:\\Users\\Lenovo\\OneDrive\\Desktop"))#to change directory
#print(os.listdir())

#random module - random module is used to generate random numbers in python, randint() is used and this function is defined in random module.
#sample
'''import random
a=random.sample(range(10,50),5)
print(a)'''

'''import random
a=random.randint(5,12)
print(a)'''

'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#ludo_game
'''import random
while True:
    roll=int(input("Roll the dice"))
    generate=random.randint(1,6)
    print(generate)
    option=int(input("choose (1/2)"))
    if option==1:
        continue
    else:
        break'''

#calendar module
'''import calendar
year=2026
month=10
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
a=int(input("Enter the year"))
b=int(input("Enter the month"))
print(calendar.month(a,b))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is:{b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"current time is:{b.tm_hour}-{b.tm_min}-{b.tm_sec}")'''

'''import random
import time
while True:
    a=random.randint(0,10)
    print(a)
    time.sleep(2)'''

'''import random
import time
for i in range(10):
    a=random.randint(0,100)
    print(a)
    time.sleep(2)'''

#regular expressions(regex) - regular expressions are powerful tools(module) embedded in python which is mainly used to find a pattern within a given string or statements or files and mainly used for text manipulation.
'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''

'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\w-> it matches alphanumeric
\W-> it matches non-alphanumeric
\d-> it matches any digit
\D-> it matches non-digits
\s-> it represents white spaces
\S-> it represents non-white spaces'''

#complie()
import re
'''a="code map money cash cap maths cup cat mug mat"'''
'''b=re.compile(r"m\w\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall()
'''b=re.findall(r"m\w+",a)
print(b)
c=re.findall(r"c\w+",a)
print(c)'''

#split()
'''c=re.split(r"m",a)
print(c)'''

'''d=re.split(r"\s",a)
print(d)'''

#sub()
'''e=re.sub(r"m","k",a)
print(e)'''

'''e=re.sub(r"maths","science",a)
print(e)'''

'''a="code 10 map money 20 cash cap 30 maths cup 40 cat mug 50 mat"
b=re.findall(r"\d+",a)
print(b)'''

'''a="code 10 map money 20 cash cap 30 maths cup 40 cat mug 50 mat"
b=re.findall(r"\d",a)
print(b)'''

a="code 10 map money 20 cash cap 30 maths cup 40 cat mug 50 mat"
b=re.findall(r"\D+",a)
print(b)









