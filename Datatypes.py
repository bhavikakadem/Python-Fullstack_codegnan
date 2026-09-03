Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #datatypes
>>> a=7
>>> type(a)
<class 'int'>
>>> b=9.0
>>> type(b)
<class 'float'>
>>> c='Python'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''Fullstack'''
>>> type(e)
<class 'str'>
>>> f=2+3j
>>> type(f)
<class 'complex'>
>>> g=True
>>> type(g)
<class 'bool'>
>>> h=False
>>> type(h)
<class 'bool'>
>>> #conversions
>>> int(45)
45
>>> int(45.18)
45
>>> int('python')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int('python')
ValueError: invalid literal for int() with base 10: 'python'
>>> int'2+3j)
SyntaxError: incomplete input
>>> int(2+3j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(2+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
float(45)
45.0
float(45.18)
45.18
float("Python")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float("Python")
ValueError: could not convert string to float: 'Python'
float(2+3j)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(2+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(6)
'6'
str(9.0)
'9.0'
str("python")
'python'
str(2+3j)
'(2+3j)'
str(True)
'True'
str(False)
'False'
complex(2)
(2+0j)
complex(2.0)
(2+0j)
complex("Python)
        
SyntaxError: incomplete input
complex("Python")
        
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex("Python")
ValueError: complex() arg is a malformed string
complex(True)
        
(1+0j)
complex(2+0j)
        
(2+0j)
complex(False)
        
0j
bool(2)
        
True
bool(2.0)
        
True
bool('python')
        
True
bool(True)
        
True
bool(False)
        
False
bool(2+3j)
        
True
