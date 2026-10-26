#email automation
#otp generation
import random
import math
import smtplib
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" "+"is your otp"
msg=otp
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("bhavikakadem@gmail.com","neky fkwm pair sill")
user="bhavikakadem@gmail.com"
email=input("Enter the mail you want to send otp:")
s.sendmail(user,email,otp)
while True:
    a=input("enter the otp")
    if a==OTP:
        print("your otp is correct")
    else:
        print("your otp is incorrect")
