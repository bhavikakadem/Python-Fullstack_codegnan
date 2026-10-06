#Generators
#Generators - no tuple comprehension in above cases if we remove those braces and keep paranthesis then the outcome is generator.
#a=[expr for var in collection/range]#list comprehension syntax
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))#generator syntax
print(a)
print(*a)
print(type(a))'''

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))
print(type(a))'''

#Def- a generator is also a function which can be used as an iterator(loop) by producing group of values where we can use yield keyword.
#diff b/w return & yield - will terminate the function where as yield can pass the function and go on with every successive iteration.
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a+=1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a+=1
        return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    return "python"
    return "java"
    return "c"
print(mygen())'''

'''def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen())

#next()
b=mygen()
print(next(b))
print(next(b))
print(next(b))'''

n=int(input())
a=[]
for i in range(n):
    a.append(i)
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(type(a))


