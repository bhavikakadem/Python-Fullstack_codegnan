Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=["code","codegnan","Python"]
>>> b=str(a)
>>> b.upper()
"['CODE', 'CODEGNAN', 'PYTHON']"
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[5:]
[4, 6, 3, 7, 0]
>>> b=a[5:0]
>>> b
[]
>>> b=a[5:]
>>> b
[4, 6, 3, 7, 0]
>>> c=a[0:5]
>>> c
[9, 1, 5, 2, 8]
>>> b.sort()
>>> b
[0, 3, 4, 6, 7]
>>> b.reverse()
>>> b
[7, 6, 4, 3, 0]
>>> c.sort()
>>> c
[1, 2, 5, 8, 9]
>>> c.reverse()
c
[9, 8, 5, 2, 1]
e=b+c
e
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
