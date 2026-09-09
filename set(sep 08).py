Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets{}
#sets are semimutable
#sets doesn't allow duplicates
#set is an unordered collection
a={5,3.9, "Python", 5+7j, True, False}
print(a)
{False, True, 3.9, 5, (5+7j), 'Python'}
type(a)
<class 'set'>
b={3,3,46,2,6,3,2,2,9}
print(b)
{2, 3, 6, 9, 46}
#set methods
a={4,5,3,3,5,2,5,8,9}
a.add(10)
a
{2, 3, 4, 5, 8, 9, 10}
#issubset
a={3,4,5,6,7,8}
b={5,6,7,8}
b.issubset(a)
True
a.issubset(b)
False
#superset
a={2,3,4,56,7,4,3,9}
b={56,7,4,3,9}
a.superset(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
#issuperset
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={1,23,3,4,5,}
b={6,7,8,9,23}
a.union(b)
{1, 3, 4, 5, 6, 7, 8, 9, 23}
#intersection
a={10,22,33,44,55}
b={5,11,55,22,4}
a.intersection(b)
{22, 55}
b.intersection(a)
{22, 55}
#update
a={2,3,4,5,67,5,8,9}
b={10,20,30,2,3,4,9}
a.update(b)
a
{2, 67, 3, 4, 5, 8, 9, 10, 20, 30}
b.update(a)
b
{2, 3, 4, 67, 5, 8, 9, 10, 20, 30}
#difference
a={2,3,4,5,6,7,8,9}
b={2,3,4,5,10,20}
a.difference(b)
{8, 9, 6, 7}
b.difference(a)
{10, 20}
#symetric difference
a={3,4,5,6,7,8,9}
b={2,3,5,3,7,10,20}
a.symetric_difference(b)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.symetric_difference(b)
AttributeError: 'set' object has no attribute 'symetric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_differene(b)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.symmetric_differene(b)
AttributeError: 'set' object has no attribute 'symmetric_differene'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{2, 4, 6, 8, 9, 10, 20}
b.symmetric_difference(a)
{2, 4, 6, 8, 9, 10, 20}
#difference_update
a={1,2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference_update(b)
a
{1, 2}
b.difference_uppdate(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b.difference_uppdate(a)
AttributeError: 'set' object has no attribute 'difference_uppdate'. Did you mean: 'difference_update'?
b.difference_update(a)
b
{3, 4, 5, 6, 7, 8}
#intersection_update
a={1,2,3,4,5,6,}
b={3,4,5,6,8,9}
a.intersection_update(b)
a
{3, 4, 5, 6}
b.intersection_update(a)
b
{3, 4, 5, 6}
#symmetric_difference_update
a={1,2,3,4,5,6,7,8,9}
b={3,4,5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{1, 2, 10, 11}
b.symmetric_difference_update(b)
b.symmetric_difference_update(a)
b
{11, 1, 2, 10}
#pop()
a={10,20,30,40,40,50}
a.pop()
50
a.pop()
20
a.pop()
40
a
{10, 30}
a.remove(30)
a
{10}
a.remove(10)
a
set()
#discard or remove
a={10,2,3,4,5,6}
a.discard(10)
a
{2, 3, 4, 5, 6}
a.discard(4)
a.remove(6)
a
{2, 3, 5}
#clear()
>>> a.clear()
>>> a
set()
>>> a.add(50)
>>> a
{50}
>>> #len()
>>> a={1,2,3,4}
>>> len(a)
4
>>> a.index(4)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(4)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
>>> #disjointa={3,4,5,6,7,8}
>>> #disjoint
>>> a={1,2,3,4,5}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
>>> c={4,5,6,7}
>>> a.isdisjoint(c)
False
