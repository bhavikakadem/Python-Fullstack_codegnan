'''credentials={"Bhavika":"bhavika@123", "Sailaja":"sailu@456", "Varshitha":"varshi@3456"}
username=input()
password=input()
if(username in credentials.keys()):
    if(password in credentials.values()):
        print("login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid credentials")'''

'''a=int(input())
if(a%3==0):
    print("FiZZ")
if(a%5==0):
    print("BUZZ")
else:
    print("Enter valid number")'''

'''a=int(input())
if(a%3==0 and a%5==0):
    print("FiZZ"+" "+"BUZZ")
elif(a%3==0):
    print("FiZZ")
elif(a%5==0):
    print("BUZZ")
else:
    print("Enter valid number")'''

'''a=int(input())
b=a%15
if(b==0):
    print("FIZZ"+" "+"BUZZ")
else:
    print("Enter")'''

'''distance=int(input())
price=0
if(distance>0):
    if(distance>=1 and distance<=8):
        price=distance*5
        print(price)
    elif(distance>=9 and distance<=15):
        price=(8*5)+(distance-8)*6
        print(price)
    elif(distance>=16 and distance<=25):
        price=(7*6)+(distance-15)*8
        print(price)
    elif(distance>=26 and distance<=30):
        price=(10*8)+(distance-25)*10
        print(price)
    elif(distance>30):
        print("Service not available")
else:
    print("Invalid data")'''

'''while True:
    n=int(input())
    option=input("(wired toys/electrical toys/battery toys)")
    if(option=="wired toys" and (n>=300 and n<=500)):
        print(n-50)
    elif(option=="wired toys" and(n>=501 and n<=900)):
        print(n-60)
    elif(option=="wired toys" and(n>=901 and n<=1500)):
        print(n-100)
    elif(option=="electrical toys" and (n>=3000 and n<=5000)):
        print(n-(n*(10/100)))
    elif(option=="electrical toys" and (n>=5001 and n<=10000)):
        print(n-(n*(15/100)))
    elif(option=="electrical toys" and (n>10000)):
        print(n-(n*(20/100)))
    else:
        print(n)'''

#Built-in methods
#max(), min(), sum()
'''a=[10,20,30,40,20,22,34]
print(max(a))
print(min(a))
print(sum(a))'''

'''students_count=int(input())
a=[]
for i in range(1,students_count+1):
    marks=int(input(f" student no.{i} marks"))
    a.append(marks)
print("Total Students:",students_count)
print("Highest marks:",max(a))
print("Lowest marks:",min(a))
print("Total marks:",sum(a))
print("Average marks:", sum(a)/students_count)'''

'''while True:
    weight=float(input())
    height=float(input())
    bmi=weight/(height**2)
    print("........BMI REPORT.......")
    if(bmi<=18.5):
        print("Under Weight")
    elif(bmi>18.5 and bmi<=24.5):
        print("Healthy Weight")
    elif(bmi>24.5 and bmi<=29.5):
        print("Over Weight")
    else:
        print("Obesity")'''

'''while True:
    def ticketp():
        ticket=1000
        gender=input("select Gender (male/female):")
        age=int(input("Enter your age:"))
        if(gender=="male" and age>=60):
            discount=ticket*(30/100)
            print(ticket-discount)
        elif(gender=="female" and age>=60):
            discount=ticket*(50/100)
            print(ticket-discount)
        elif(gender=="female" and age<60):
            discount=ticket*(30/100)
            print(ticket-discount)
        else:
            print(ticket)
    ticketp()'''

'''while True:
    price=int(input("Enter price value:"))
    cupon=int(input("Enter cupon number:"))
    if(cupon==1):
        discount=price*(100/100)
        print(price-discount)
    elif(cupon==2):
        discount=price*(50/100)
        print(price-discount)
    elif(cupon==3):
        discount=price*(10/100)
        print(price-discount)
    else:
        print("Enter valid cupon")'''

'''while True:
    n=int(input())
    option=int(input("select (1/2/3):"))
    if option==1:
        for i in range(1,11):
            print(str(n)+"*"+str(i)+"="+str(n*i))
    elif option==2:
        for i in range(1,21):
            print(str(n)+"*"+str(i)+"="+str(n*i))
    else:
        for i in range(1,n+1):
            for j in range(1,11):
                print(str(i)+"*"+str(j)+"="+str(i*j))'''




                
    
    


        









