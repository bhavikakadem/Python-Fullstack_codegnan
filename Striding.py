Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Striding
a="data Science"
a[::]
'data Science'
a[::1]
'data Science'
a[::2]
'dt cec'
b="Machine Learning"
b[::9]
'Me'
a[::3]
'dacn'
b[::3]
'Mheeng'
>>> a[::5]
'dSc'
>>> b[::5]
'Mnag'
>>> b[::2]
'McieLann'
>>> b[::9]
'Me'
>>> b[3:11]
'hine Lea'
>>> b[5:]
'ne Learning'
>>> b[:7]
'Machine'
>>> c="Cloud Computing"
>>> c[1:7:2]
'lu '
>>> c[4:14:5]
'dp'
>>> c[3:12:6]
'up'
>>> c[2:13:3]
'o mt'
>>> #Negative Striding
>>> a="Python Course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sCh'
>>> a[-4:-13:-5]
'uo'
>>> a[-6:-12:-2]
'Cnh'
>>> #In positive striding highest to lowest is not possible
>>> #In Negative striding lowest to highest is not possible
>>> d="Python course"
>>> a[7:3:2]
''
>>> a[3:7:2]
'hn'
>>> a[-9:-5:-2]
''
>>> a[::1]
'Python Course'
>>> a[::-1]
'esruoC nohtyP'
