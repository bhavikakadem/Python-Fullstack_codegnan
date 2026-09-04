Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Arithematic Operations
a=5
b=10
print(a+b)
15
print(b-a)
5
print(a-b)
-5
print(a*b)
50
print(a//b)
0
print(a/b)
0.5
print(a**b)
9765625
print(a%b)
5
#Assignment operations
a=3
b=6
a+=b
a
9
a-=2
a
7
a*3
21
a//b
1
a*=3
a
21
a//=b
a
3
a/=b
a%=b
a
0.5
a/=b
a
0.08333333333333333
b+=a
b
6.083333333333333
b-=a
b
6.0
b*=2
b
12.0
b/=2
b
6.0
b//=2
b%=2
b
1.0
b//=2
b
0.0
#Comparision
a=45
b=20
a>b
True
b<a
True
a!=b
True
b!=a
True
a==b
False
a<=b
False
b>=a
False
b<=a
True
a>=b
True
a<b
False
b>a
False
#Logical
a=5
b=10
a<b and b>a
True
a>b and b>a
False
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b<=a
True
a!b or a==b
SyntaxError: invalid syntax
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
a=45
type(a) is int
True
type(a) is float
False
type(a) is not float
True
type(a) is string'
SyntaxError: incomplete input
type(a) is st
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    type(a) is st
NameError: name 'st' is not defined. Did you mean: 'set'?
type(a) is str
False
type(a) is not str
True
type(a) is bool
False
type(a) is not bool
True
type(a) is not complex
True
b=45.0
type(b) is float
True
type(b) is not str
True
type(b) is not bool
True
type(b) is not int
True
type(b) is complex
False
#membership
a=10,17,18,45,63,93
45 in a
True
10 in a
True
28 in a
False
45 not in a
False
17 in a
True
18 not in a
False
63 in a
True
93 not in a
False
a=2
b=6
a&b
2
a=3
b=8
a|b
11
>>> a=9
>>> b=7
>>> a|b
15
>>> #Bitwise not
>>> # -(x+1)
>>> a=3
>>> ~a
-4
>>> a=-5
>>> `a
SyntaxError: invalid syntax
>>> ~a
4
>>> #XOR
>>> a=3
>>> b=2
>>> a^b
1
>>> a=6
>>> b=8
>>> a^b
14
>>> #Left shit <<
>>> a=4
>>> b=2
>>> a<<b
16
>>> a=8
>>> b=2
>>> a<<b
32
>>> #Right shigt >>
>>> a=3
>>> b=2
>>> a>>b
0
>>> a=7
>>> b=3
>>> a>>b
0
>>> a=7
>>> b=2
>>> a>>b
1
