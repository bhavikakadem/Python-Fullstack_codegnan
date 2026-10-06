#Loops
# In python we have total 6-loops. They are
#for, while, range, break, continue, pass
#for loop()- sequence iteration
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50,60]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50,60]
for i in a:
    print(i,"end")'''# this is wrong

'''a=[10,20,30,40,50,60]
for i in a:
    print(i, end="")'''

'''a=[10,20,30,40,50,60]
for i in a:
    print(i, end=" ")'''

'''a=[10,20,30,40,50,60]
for i in a:
    print(i)
print(type(a))'''

'''a=[10,20,30,40,50,60]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(6,7,8,9,10)
for i in a:
   print(i)
   print(type(a))
   print(type(i))'''

'''a={4,5,6,6,7,8,9,9}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={"year":2026, "month":"sep", "date":16}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[2.3,1.2,4.3,5.6]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=["Python", "Java", "c"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''


'''a=[2+3j, 4+5j, 3+7j]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[True, False]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[10,"java",2.5, 4+5j, True]
for i in a:
    print(i)
    print(type(a))
print(type(i))'''

'''a=["apple","banana","grapes"]
b=str(a)
c=list(b.upper())
for i in c:
    print(i, end="")'''
    
'''a=["apple","banana","grapes"]
b=str(a)
for i in b.upper():
    print(i, end="")'''

'''a='a'
print(ord('a'))'''

'''a=["apple","banana","grapes"]
b=[]
for i in a:
    b.append(i.upper())
print(b)'''

'''for i in range(65,68,1):
    for j in range (3):
        print(chr(i),end=" ")
    print()'''

'''for i in range(67,64,-1):
    for j in range (3):
        print(chr(i),end=" ")
    print()'''

#While loop-continue iteration
'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=20
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    print(a)
    a=a-1'''

'''a=15
while a>2:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''while True:
    age=int(input())
    if(age>=18):
        print("They are eligible to vote")
    else:
        print("They are not eligible")'''

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=5
while a<15:
    print(a)
    a+=1'''

#range()-sequence iteration
#The range function returns a sequence of numbers, starting from '0' by default and increments by one by one and stops before a specify number.
    
'''for i in range(10):
    print(i)'''

'''for i in range(15,30):
    print(i)'''

'''for i in range(0,20,2):
    print(i,end=",")'''

'''for i in range(5,50,5):
    print(i,end=",")'''

'''for i in range(3,30,3):
    print(i,end=",")'''

'''while True:
    marks=int(input())
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")'''

'''while True:
    n=int(input())
    p=0
    ab=0
    for i in range(n):
        c=input(f" student {i} (p/a)")
        if(c=='p'):
            p+=1
        else:
            ab+=1
    print("Attendance Tracker......")
    print("No. of students:",n)
    print("No. of presenties:",p)
    print("No. of absenties:",ab)'''

#break - the break statement is used to terminate the entire loop.
#continue - the continue statement is used to skips the current iteration and rest of the code will continue.
#pass -  a pass is a null statement it does nothing but syntatically we need.
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==4:
        break
    print(a)'''

'''for i in range(10):
    if i==8:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(i)''' #error-break,continue,pass should be used in only loops not in condition statements itself.

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    a=a-1
    if a==12:
        continue
    print(a)'''

'''for i in range(15):
    if i==10:
        continue
    print(i)'''

'''a="python"
for i in a:
    if(i=="y"):
        continue
    print(i)'''

#pass
'''a=5
while a>1:
    print(a)
    a=a-1
    if a==2:
        pass'''

'''for i in range(25):
    if i==10:
        pass
    print(i)'''




    








    

