Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#replace
a="wait until you succeed"
a.replace("wait", "work")
'work until you succeed'
#upper()
b="Python"
b.upper()
'PYTHON'
c="JAVA"
c.upper()
'JAVA'
#lower()
d="INDIA"
d.lower()
'india'
#capitalize()
c="java"
c.capitalize()
'Java'
#title()
e="vijayawada is a royal city"
e.title()
'Vijayawada Is A Royal City'
#conditions
a="hello world"
a.startswith("h")
True
#startswith
a="India"
a.startswith("I")
True
#endswith
a="hello world"
a.endswith("d")
True
#isalpha()
r="RohitSharma"
r.isaplha()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    r.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
r.isalpha()
True
r="Vjayawada is a royal city"
r.isalpha()
False
#isdigit()
num="1235"
num.isdigit()
True
str=23456
str.isdigit()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    str.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
str="la1234"
str.isdigit()
False
#isalnum()
country="India"
country.isalnum()
True
num="bhavi2345"
num.isalnum()
True
#strip() is used to remove white spaces
#lstrip(), rstrip()
name="          Bhavika       "
name.strip()
'Bhavika'
str="          Bhavika"
str.lstrip()
'Bhavika'
d="Bhavika      "
d.rstrip()
'Bhavika'
str.rstrip()
'          Bhavika'
#concatenation
a="code"
b=gnan"
SyntaxError: incomplete input
b="gnan"
print(a+b)
codegnan
fname="bhavika"
lname="kadem"
print(fname+lname)
bhavikakadem
print(fname+" "+lname)
bhavika kadem
print(fname.title()+" "+lname.title())
Bhavika Kadem
print((fname+" "+lname).title())
Bhavika Kadem
#split()
a="Python java c c++"
a.split()
['Python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']
d="vij", "hyd", "vzg"
#join
"".join(d)
'vijhydvzg'
" ".join(d)
'vij hyd vzg'
"1".join(d)
'vij1hyd1vzg'
"1 ".join(d)
'vij1 hyd1 vzg'
e="hello"
"m".join(e)
'hmemlmlmo'
"formatting
SyntaxError: incomplete input
#formatting
a=5
b=7
print(a+b)
12
print("The sum is:", a+b)
The sum is: 12
city="Vja"
print("city is:", city)
city is: Vja
#format()
a="motu"
b="pathlu"
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a.b))
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    print("hello {} {}".format(a.b))
AttributeError: 'str' object has no attribute 'b'
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {} hello {}".format(a,b))
hello motu hello pathlu
#fstring()
a="Rohit"
>>> b="sharma"
>>> print(f"hello{a}{b}")
helloRohitsharma
>>> print(f" hello {a} {b}")
 hello Rohit sharma
>>> print(f" hello {a} hello{b}")
 hello Rohit hellosharma
>>> print(f" hello {a} hello {b}")
 hello Rohit hello sharma
>>> fname="Bhavika"
>>> lname="Kadem"
>>> print("Hi {}{}."format(fname,lname))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("Hi {}{}".format(fname,lname))
Hi BhavikaKadem
>>> print("Hi {} {}".format(fname,lname))
Hi Bhavika Kadem
>>> print(f"Hi {fname} {lname}")
Hi Bhavika Kadem
>>> print(f"Hi, {fname} {lname}")
Hi, Bhavika Kadem
>>> a=2
>>> b=2
>>> print("sum is: {}".format(a+b))
sum is: 4
>>> c=a=+b
>>> print(f"sum is: {c}")
sum is: 2
>>> c=a+b
>>> print(f"sum is: {c}")
sum is: 4
