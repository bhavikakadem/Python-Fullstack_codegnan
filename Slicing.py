Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Slicing
a="Codegnan"
>>> a[0:4]
'Code'
>>> a[4:8]
'gnan'
>>> a[:4]
'Code'
>>> a[4:]
'gnan'
>>> b="work until you succeed"
>>> b[5:10]
'until'
>>> b[15:]
'succeed'
>>> b[11:14]
'you'
>>> b[:4]
'work'
>>> c="Vijayawada is a royal city"
>>> c[22:]
'city'
>>> c[16:21]
'royal'
>>> c[:10]
'Vijayawada'
>>> c[11:13]
'is'
>>> #Negative slicing
>>> a="Happy Teachers Day"
>>> a[-18:-15]
'Hap'
>>> a[-18:-14]
'Happ'
>>> a[-18:-13]
'Happy'
>>> a[-12:-4]
'Teachers'
>>> a[-3:]
'Day'

>>> b="Vizag is a city of Destiny"
>>> b[:-21]
'Vizag'
>>> b[-15:-11]
'city'
>>> b[-7:]
'Destiny'
