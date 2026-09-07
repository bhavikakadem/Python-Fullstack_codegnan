Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#String Methods
#len()
a="Python"
len(a)
6
b="Python Course"
len(b)
13
c=""
len(c)
0
c=" "
len(c)
1
#count()
a="Boy"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
#count is not a built-in function, it is a method.
a.count('b')
0
a.count('B')
1
b="Twinkle Twinkle Little Star"
b.count("star")
0
>>> b.count("Star")
1
>>> b.count("Twinkle")
2
>>> b.count("Little")
1
>>> #find a string
>>> a="Python"
>>> a.find("o")
4
>>> a.find("P")
0
>>> a.find("Y")
-1
>>> a.find("y")
1
>>> #find() is used to find the index position of a letter
>>> #while using find method if there are repeated letters then it consider first letter index only.
>>> #Escape sequences
>>> #\n-> new line
>>> #\t -> tab space
>>> a="idno\nname\t mobileno\nmailid\nbranch\tcollege"
>>> print(a)
idno
name	 mobileno
mailid
branch	college
>>> a="idno:45\n Name: Bhavika\t Mobileno: 6394208392\tmailid:bhavikak@gmail.com\nBranch: CSE - Data Science\t College: VNITSW"
>>> print(a)
idno:45
 Name: Bhavika	 Mobileno: 6394208392	mailid:bhavikak@gmail.com
Branch: CSE - Data Science	 College: VNITSW
\
>>> a="idno:45\nName: Bhavika\t Mobileno: 6394208392\tmailid:bhavikak@gmail.com\nBranch: CSE - Data Science\t College: VNITSW"
>>> print(a)
idno:45
Name: Bhavika	 Mobileno: 6394208392	mailid:bhavikak@gmail.com
Branch: CSE - Data Science	 College: VNITSW
>>> a="idno:45\nName: Bhavika\nMobileno: 6394208392\nmailid:bhavikak@gmail.com\nBranch: CSE - Data Science\nCollege: VNITSW"
>>> print(a)
idno:45
Name: Bhavika
Mobileno: 6394208392
mailid:bhavikak@gmail.com
Branch: CSE - Data Science
College: VNITSW
