Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#List[]
a=[3,2.5,"Python", 2+3j, True, False]
print(a)
[3, 2.5, 'Python', (2+3j), True, False]
type(a)
<class 'list'>
b=45.2
type(b)
<class 'float'>
b[45.2]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b[45.2]
TypeError: 'float' object is not subscriptable
b=45.2
type(b)
<class 'float'>
b=[45.2]
type(b)
<class 'list'>
c=45
c=[35]
type(c)
<class 'list'>
s="Python"
type(s)
<class 'str'>
s=["Python"]
type(s)
<class 'list'>
#list methods
#append
a=["Python", "Java", "C"]
a.append("ML")
a
['Python', 'Java', 'C', 'ML']
a.append("HTML", "CSS")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.append("HTML", "CSS")
TypeError: list.append() takes exactly one argument (2 given)
a
a.append(["HTML", "CSS"])
a
['Python', 'Java', 'C', 'ML', ['HTML', 'CSS']]
#extend
b=["HTML", "CSS", "JavaScript"]
b.extend("Python","Java")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b.extend("Python","Java")
TypeError: list.extend() takes exactly one argument (2 given)
b.extend["Python","Java"]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b.extend["Python","Java"]
TypeError: 'builtin_function_or_method' object is not subscriptable

b.extend(["Python","Java"])
b
['HTML', 'CSS', 'JavaScript', 'Python', 'Java']
country=["India", "Swiss", "canada"]
country.extend(["UK", "USA"])
country
['India', 'Swiss', 'canada', 'UK', 'USA']
#insert
colours=["Blue","Red","Orange"]
colours.insert(2,"Green")
colours
['Blue', 'Red', 'Green', 'Orange']
fruits=["Sapota","Orange","Grapes"]
fruits.insert(2,"Papaya")
fruits
['Sapota', 'Orange', 'Papaya', 'Grapes']
#index
fruits.index("Sapota")
0
fruits.index("Grapes")
3
fruits.index("Papaya")
2
#copy
fruits.copy()
['Sapota', 'Orange', 'Papaya', 'Grapes']
food=fruits.copy()
food
['Sapota', 'Orange', 'Papaya', 'Grapes']
a=["Hi","Hello","How","Are","You"]
#pop is used to delete the data if we use pop() it will delete the last element in the list
a.pop()
'You'
a
['Hi', 'Hello', 'How', 'Are']
#if we want to delete the data at particular position then we use pop(index number) like pop(0), pop(1)..
a.pop(2)
'How'
a
['Hi', 'Hello', 'Are']
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.pop(3)
IndexError: pop index out of range
a.pop(0)
'Hi'
a
['Hello', 'Are']
a.pop(1)
'Are'
a
['Hello']
#remove
#remove is used to delete the data by using element name
a.remove("Hello")
a
[]
#sort()
a=["India","UK","USA","Canada","Brazil","Argentina"]
a.sort()
a
['Argentina', 'Brazil', 'Canada', 'India', 'UK', 'USA']
n=[2,4,46,2,67,34,0987,68,9876]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
n=[2,4,46,2,67,34,987,68,9876]
n.sort()
n
[2, 2, 4, 34, 46, 67, 68, 987, 9876]
>>> c=[2,3.0,"Python",3+4j,True,False]
>>> c.sort()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
>>> #reverse
>>> a.reverse()
>>> a
['USA', 'UK', 'India', 'Canada', 'Brazil', 'Argentina']
>>> #len()
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(a)
6
>>> a.count("Argentina")
1
>>> b="Java"
>>> len(b)
4
>>> #clear()
>>> a=["Python",".net","Java"]
>>> a.clear()
>>> a
[]
>>> a.append("HTML")
>>> a
['HTML']
