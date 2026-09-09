Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple()
>>> #typle is immutable
>>> #we cannot change the data once we can create
>>> a=(5,2.0,4+5j,"Python",True,False)
>>> print(a)
(5, 2.0, (4+5j), 'Python', True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.count("Python")
1
>>> a.index(True)
4
