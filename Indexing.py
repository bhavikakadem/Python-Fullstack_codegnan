Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Indexing
a='VIjayawada'
a[0]
'V'
a[2]
'j'
a[4]
'y'
>>> b="Hitman The Rohit Sharma"
>>> b[2]
't'
>>> b[0]+b[1]+b[2]+b[3]+b[4]+b[5]
'Hitman'
>>> b[6]
' '
>>> b[7]+b[8]+b[9]+b[10]+b[11]
'The R'
>>> b[11]+b[12]+b[13]+b[14]+b[15]
'Rohit'
>>> b[11]+b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]+b[21]+b[22]
'Rohit Sharma'
>>> a="I am Learning python fullstack"
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]
'fullstack'
>>> a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'Learning'
>>> a[0]+a[1]+a[2]+a[3]
'I am'
>>> a[2]+a[3]
'am'
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'Learn'
>>> a="Time is very Precious"
>>> a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Precious'
>>> a[-13]+a[-12]+a[-11]+a[-10]
'very'
>>> a[-18]+a[-19]+a[-20]+a[-21]
'emiT'
>>> a[-21]+a[-20]+a[-19]+a[-18]
'Time'
>>> a="Codegnan IT Solutions
SyntaxError: incomplete input
>>> a="Codegnan IT Solutions"
>>> a[-21]+a[-20]+a[-19]+a[-18]
'Code'
>>> a[-17]+a[-16]+a[-15]+a[-14]
'gnan'
>>> a[-9]+a[-8]+a[--7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Sonutions'
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Solutions'
